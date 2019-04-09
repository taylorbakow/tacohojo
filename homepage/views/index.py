from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from decimal import Decimal
from homepage import models as hmod
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    if request.method == 'POST':
        if 'Prescriber' in request.POST:
            name = request.POST['prescribername']
            sList = hmod.Prescriber.objects.filter(Fname__icontains=name) | hmod.Prescriber.objects.filter(Lname__icontains=name)
            sList
            formP = PrescriberForm()
            formD = DrugForm()
            objectType = 'Prescriber'
        elif 'Drug' in request.POST:
            name = request.POST['drugname']
            sList = hmod.Opioids.objects.filter(DrugName=name)
            formP = PrescriberForm()
            formD = DrugForm()
            objectType = 'Drug'
    else:
        formP = PrescriberForm()
        formD = DrugForm()
        sList = []
        objectType = ''

    context = {
        'formP': formP,
        'formD': formD,
        'sList': sList,
        'objectType': objectType,
    }
    return request.dmp.render('index.html', context)

class PrescriberForm(forms.Form):
    prescribername = forms.CharField(label='Prescriber', widget=forms.TextInput(attrs={'class' : 'form-control'}))

class DrugForm(forms.Form):
    drugname = forms.CharField(label='Drug', widget=forms.TextInput(attrs={'class' : 'form-control'}))

