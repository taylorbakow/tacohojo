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
    formP = CreateOrEditForm()

    if request.method == 'POST':
        print('test')
        form = CreateOrEditForm(request.POST)

        if form.is_valid():
            print('test111')
            p = hmod.Prescriber()
            p.Fname = form.cleaned_data.get("Fname")
            p.Lname = form.cleaned_data.get("Lname")
            p.Gender = form.cleaned_data.get("Gender")
            p.Credentials = form.cleaned_data.get("Credentials")
            p.Specialty = form.cleaned_data.get("Specialty")
            p.OpioidPrescriber = form.cleaned_data.get("OpioidPrescriber")
            p.StateAbbrev = form.cleaned_data.get("StateAbbrev")
            p.TotalPrescription = form.cleaned_data.get("TotalPrescription")
            p.AcetaminophinCodeine = form.cleaned_data.get("AcetaminophinCodeine")
            p.Fentanyl = form.cleaned_data.get("Fentanyl")
            p.HydrocodoneAcetaminophen = form.cleaned_data.get("HydrocodoneAcetaminophen")
            p.OxycodoneAcetaminophen = form.cleaned_data.get("OxycodoneAcetaminophen")
            p.Oxycontin = form.cleaned_data.get("Oxycontin")
            p.save()
            return HttpResponseRedirect('/homepage/managedata.html')
        else:
           raise forms.ValidationError("You are fired")
    else:
        form = CreateOrEditForm()

    context={
        'formP': formP,
    }
    return request.dmp.render('managedata.create.html', context)

@view_function
def delete(request, pid):
    return process_request(request)

@view_function
def edit(request, pid):
    # eform = EditForm()
    prescriber = hmod.Prescriber.objects.get(id=pid)

    context={
        'prescriber': prescriber,
        # 'eform': eform,
    }
    return request.dmp.render('managedata.edit.html', context)

class PrescriberForm(forms.Form):
        prescribername = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Prescriber', 'placeholder' :'Search by Prescriber', 'style' : 'width: 90%;'}), required=False)

class CreateOrEditForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    Fname = forms.CharField(label="First Name", required=True)
    Lname = forms.CharField(label="Last Name", required=True)
    Gender = forms.ChoiceField(label="Gender", widget=forms.Select(), required=True, choices=GENDER_CHOICES)
    Credentials = forms.CharField(label="Credentials", required=True)
    Specialty = forms.CharField(label="Specialty", required=True)
    OpioidPrescriber = forms.BooleanField(label="Opioid Prescriber?")
    StateAbbrev = forms.ModelChoiceField(queryset=hmod.Prescriber.objects.order_by("StateAbbrev__StateAbbrev").values_list("StateAbbrev__StateAbbrev", flat=True).distinct(), label="State", widget=forms.Select(), required=True)
    TotalPrescription = forms.IntegerField(label="Total Prescription", required=True)
    AcetaminophinCodeine = forms.IntegerField(label="# Acetaminophin.Codeine Prescribed", required=False)
    Fentanyl = forms.IntegerField(label="# Fentanyl Prescribed", required=False)
    HydrocodoneAcetaminophen = forms.IntegerField(label="# Hydrocodone.Acetaminophen Prescribed", required=False)
    OxycodoneAcetaminophen = forms.IntegerField(label="# Oxycodone.Acetaminophen Prescribed", required=False)
    Oxycontin = forms.IntegerField(label="# Oxycontin Prescribed", required=False) 
