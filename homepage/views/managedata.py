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

class PrescriberForm(forms.Form):
        prescribername = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Prescriber', 'placeholder' :'Search by Prescriber', 'style' : 'width: 90%;'}), required=False)

@view_function
def create(request):

    return request.dmp.render('managedata.create.html')

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

    # class EditForm(forms.Form): 
    #     Fname = forms.CharField()
    #     Lname = forms.CharField()
    #     Gender = forms.CharField(max_length=1)
    #     Credentials = forms.CharField()
    #     Specialty = forms.CharField()
    #     OpioidPrescriber = forms.BooleanField()
    #     StateAbbrev = forms.CharField(max_length=2)
    #     TotalPrescription = forms.IntegerField()
    #     AcetaminophinCodeine = forms.IntegerField(default=0)
    #     Fentanyl = forms.IntegerField(default=0)
    #     HydrocodoneAcetaminophen = forms.IntegerField(default=0)
    #     OxycodoneAcetaminophen = forms.IntegerField(default=0)
    #     Oxycontin = forms.IntegerField(default=0) 
