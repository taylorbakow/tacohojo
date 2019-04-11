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
    return process_request(request)

@view_function
def edit(request, pid):
    prescriber = hmod.Prescriber.objects.get(id=pid)
    if request.method == 'POST':
        print('test')
        form = CreateOrEditForm(request.POST, instance=prescriber)

        if form.is_valid():
            print('test111')
            prescriber.Fname = request.POST["Fname"]            
            prescriber.Lname = request.POST["Lname"]
            prescriber.Gender = request.POST["Gender"]
            prescriber.Credentials = request.POST["Credentials"]
            prescriber.Specialty = request.POST["Specialty"]
            prescriber.OpioidPrescriber = request.POST["OpioidPrescriber"]
            prescriber.StateAbbrev = request.POST["StateAbbrev"]
            prescriber.TotalPrescription = request.POST["TotalPrescription"]
            prescriber.AcetaminophinCodeine = request.POST["AcetaminophinCodeine"]
            prescriber.Fentanyl = request.POST["Fentanyl"]
            prescriber.HydrocodoneAcetaminophen = request.POST["HydrocodoneAcetaminophen"]
            prescriber.OxycodoneAcetaminophen = request.POST["OxycodoneAcetaminophen"]
            prescriber.Oxycontin = request.POST["Oxycontin"]
            prescriber.save()
            return HttpResponseRedirect('/homepage/managedata.html')
        else:
           raise forms.ValidationError("You are fired")
    else:
        form = CreateOrEditForm()

    context={
        'form': form,
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
