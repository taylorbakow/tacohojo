from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from decimal import Decimal
from homepage import models as hmod
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from account import models as amod
from django.contrib.auth import models as pmod
from django.db.models import Q 

@view_function
def process_request(request):
    formP = PrescriberForm()
    pList = []
    objectType = ''
    if request.method == 'POST':
        print('test')
        if len(request.POST['prescribername']) > 0:
            print('prescriber')
            pname = request.POST['prescribername']
            pList = hmod.Prescriber.objects.filter( Q(Fname__icontains=pname) | Q(Lname__icontains=pname)).distinct()[0:10]
            objectType = 'Prescriber'
    else:
        pass

    context = {
        'formP': formP,
        'pList': pList,
        'objectType': objectType,
    }
    return request.dmp.render('managedata.html', context)

@view_function
def create(request):
    if request.method == 'POST':
        print('test')
        form = CreateOrEditForm(request.POST)
        print('test111')
        p = hmod.Prescriber()
        p.Fname = request.POST["Fname"]            
        p.Lname = request.POST["Lname"]
        p.Gender = request.POST["Gender"]
        p.Credentials = request.POST["Credentials"]
        p.Specialty = request.POST["Specialty"]
        p.OpioidPrescriber = request.POST["OpioidPrescriber"]
        p.StateAbbrev = hmod.States.objects.get(StateAbbrev=request.POST["StateAbbrev"])
        p.TotalPrescription = request.POST["TotalPrescription"]
        p.AcetaminophinCodeine = request.POST["AcetaminophinCodeine"]
        p.Fentanyl = request.POST["Fentanyl"]
        p.HydrocodoneAcetaminophen = request.POST["HydrocodoneAcetaminophen"]
        p.OxycodoneAcetaminophen = request.POST["OxycodoneAcetaminophen"]
        p.Oxycontin = request.POST["Oxycontin"]
        p.save()
        return HttpResponseRedirect('/homepage/managedata')
    else:
        form = CreateOrEditForm()

    context={
        'form': form,
    }
    return request.dmp.render('managedata.create.html', context)

@view_function
def delete(request, pid):
    hmod.Prescriber.objects.get(id=pid).delete()
    return HttpResponseRedirect('/homepage/managedata')

@view_function
def edit(request, pid):
    prescriber = hmod.Drugs_Details.objects.filter(PrescriberID_id=pid).first()
    dlist = hmod.Drugs_Details.objects.filter(PrescriberID_id=pid)
    if request.method == 'POST':
        if request.POST["NumDrugs"] is None:
            print('test')
            form = EditForm(request.POST)
            formd = EditDrug()
            prescriber.PrescriberID.id = pid
            if request.POST["Fname"] is not '':
                prescriber.PrescriberID.Fname = request.POST["Fname"] 
            if request.POST["Lname"] is not '':           
                prescriber.PrescriberID.Lname = request.POST["Lname"]
            if request.POST["Gender"] is not '':
                prescriber.PrescriberID.Gender = request.POST["Gender"]
            if request.POST["Credentials"] is not '':
                prescriber.PrescriberID.Credentials = request.POST["Credentials"]
            if request.POST["Specialty"] is not '':
                prescriber.PrescriberID.Specialty = request.POST["Specialty"]
            if request.POST["OpioidPrescriber"] is not '':
                prescriber.PrescriberID.OpioidPrescriber = request.POST["OpioidPrescriber"]
            if request.POST["StateAbbrev"] is not '':
                prescriber.PrescriberID.StateAbbrev = request.POST["StateAbbrev"]
            prescriber.PrescriberID.save()
            return HttpResponseRedirect('/homepage/managedata')
        else:
            form = EditForm()
            formd = EditDrug(request.POST)
            drugid =  request.POST["id"]
            drugamt = hmod.Drugs_Details.objects.filter(PrescriberID_id=pid, DrugID_id=drugid).first()
            drugamt.QtyPrescribed = request.POST["NumDrugs"]
            drugamt.save()
            return HttpResponseRedirect('/homepage/managedata')
                
    else:
        form = EditForm()
        formd = EditDrug()

    context={
        'form': form,
        'formd': formd,
        'dlist': dlist,
        'prescriber': prescriber,
    }
    return request.dmp.render('managedata.edit.html', context)

class PrescriberForm(forms.Form):
    prescribername = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Prescriber', 'placeholder' :'Search by Prescriber', 'style' : 'width: 90%;'}), required=False)

class CreateOrEditForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    BOOLEAN_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    Fname = forms.CharField(label="First Name", required=True)
    Lname = forms.CharField(label="Last Name", required=True)
    Gender = forms.ChoiceField(label="Gender", required=True, widget=forms.Select(), choices=GENDER_CHOICES)
    Credentials = forms.CharField(label="Credentials", required=True)
    Specialty = forms.CharField(label="Specialty", required=True)
    OpioidPrescriber = forms.ChoiceField(label="Opioid Prescriber?", required=True, widget=forms.Select(), choices=BOOLEAN_CHOICES)
    StateAbbrev = forms.ModelChoiceField(queryset=hmod.Prescriber.objects.order_by("StateAbbrev__StateAbbrev").values_list("StateAbbrev__StateAbbrev", flat=True).distinct(), label="State", widget=forms.Select(), required=True)
    TotalPrescription = forms.IntegerField(label="Total Prescription", required=True)
    AcetaminophinCodeine = forms.IntegerField(label="# Acetaminophin.Codeine Prescribed", required=False)
    Fentanyl = forms.IntegerField(label="# Fentanyl Prescribed", required=False)
    HydrocodoneAcetaminophen = forms.IntegerField(label="# Hydrocodone.Acetaminophen Prescribed", required=False)
    OxycodoneAcetaminophen = forms.IntegerField(label="# Oxycodone.Acetaminophen Prescribed", required=False)
    Oxycontin = forms.IntegerField(label="# Oxycontin Prescribed", required=False) 


class EditForm(forms.Form):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    BOOLEAN_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    Fname = forms.CharField(label="First Name", required=False)
    Lname = forms.CharField(label="Last Name", required=False)
    Gender = forms.ChoiceField(label="Gender", required=False, widget=forms.Select(), choices=GENDER_CHOICES)
    Credentials = forms.CharField(label="Credentials", required=False)
    Specialty = forms.CharField(label="Specialty", required=False)
    OpioidPrescriber = forms.ChoiceField(label="Opioid Prescriber?", required=False, widget=forms.Select(), choices=BOOLEAN_CHOICES)
    StateAbbrev = forms.ModelChoiceField(queryset=hmod.Prescriber.objects.order_by("StateAbbrev__StateAbbrev").values_list("StateAbbrev__StateAbbrev", flat=True).distinct(), label="State", widget=forms.Select(), required=False)

class EditDrug(forms.Form):
    NumDrugs = forms.IntegerField(label="", required=False, widget=forms.TextInput(attrs={'class' : 'col-1', 'style':'width: 30px;'}))
