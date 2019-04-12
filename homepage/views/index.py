from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from decimal import Decimal
from homepage import models as hmod
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.db.models import Q 

@view_function
def process_request(request):
    if request.user.is_authenticated:
        formP = PrescriberForm()
        formD = DrugForm()
        pList = []
        dList = []
        objectType = ''
        ddList = []

        if request.method == 'POST':
            print('test')
            if len(request.POST['prescribername']) > 0 and len(request.POST['drugname']) > 0:
                pname = request.POST['prescribername']
                dname = request.POST['drugname']
                attr = request.POST['attribute']
                if attr == 'Name':
                    pList = hmod.Prescriber.objects.filter( Q(Fname__icontains=pname) | Q(Lname__icontains=pname)).distinct()[0:10]
                elif attr == 'Credentials':
                    pList = hmod.Prescriber.objects.filter( Q(Credentials__icontains=pname)).distinct()[0:10]
                elif attr == 'Specialty':
                    pList = hmod.Prescriber.objects.filter( Q(Specialty__icontains=pname)).distinct()[0:10]
                elif attr == 'Gender':
                    pList = hmod.Prescriber.objects.filter( Q(Gender__icontains=pname)).distinct()[0:10]
                else:
                    pList = hmod.Prescriber.objects.filter( Q(StateAbbrev=pname)).distinct()[0:10]

                dList = hmod.Opioids.objects.filter(DrugName__icontains=dname).distinct()[0:10]
                pidList = []
                didList = []
                for p in pList:
                    pidList.append(p.id)
                for d in dList:
                    didList.append(d.id)
                ddList = hmod.Drugs_Details.objects.filter(DrugID__in=didList, PrescriberID__in=pidList)[0:10]
                objectType = 'Both'
                print('Hooray')
            elif len(request.POST['prescribername']) > 0:
                print('prescriber')
                pname = request.POST['prescribername']
                attr = request.POST['attribute']
                if attr == 'Name':
                    pList = hmod.Prescriber.objects.filter( Q(Fname__icontains=pname) | Q(Lname__icontains=pname)).distinct()[0:10]
                elif attr == 'Credentials':
                    pList = hmod.Prescriber.objects.filter( Q(Credentials__icontains=pname)).distinct()[0:10]
                elif attr == 'Specialty':
                    pList = hmod.Prescriber.objects.filter( Q(Specialty__icontains=pname)).distinct()[0:10]
                elif attr == 'Gender':
                    pList = hmod.Prescriber.objects.filter( Q(Gender__icontains=pname)).distinct()[0:10]
                else:
                    pList = hmod.Prescriber.objects.filter( Q(StateAbbrev=pname)).distinct()[0:10]
                objectType = 'Prescriber'
            elif len(request.POST['drugname']) > 0:
                print('drug')
                dname = request.POST['drugname']
                if request.POST['isopiod'] == 'on':
                    dList = hmod.Opioids.objects.filter(DrugName__icontains=dname, IsOpioid='True')[0:10]
                else:
                    dList = hmod.Opioids.objects.filter(DrugName__icontains=dname).distinct()[0:10]
                objectType = 'Drug'
        else:
            pass

        context = {
            'formP': formP,
            'formD': formD,
            'pList': pList,
            'dList': dList,
            'objectType': objectType,
            'ddList': ddList,
        }
        return request.dmp.render('index.html', context)
    else:
        return HttpResponseRedirect('/account/login')

class PrescriberForm(forms.Form):
    attr = [
        ("Name", "Name"),
        ("Credentials", "Credentials"),
        ("Specialty", "Specialty"), 
        ("Gender", "Gender"), 
        ("State", "State"), 
    ]
    prescribername = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Prescriber', 'placeholder' :'Search Prescriber'}), required=False)
    attribute = forms.CharField(label='', widget=forms.Select(choices=attr, attrs={'class' : 'form-control', 'style' : 'width: 155px; margin-left: 162px; margin-top:5px;'}))

class DrugForm(forms.Form):
    drugname = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Drug', 'placeholder' :'Search by Drug Name'}), required=False)
    isopiod = forms.BooleanField(required=False, label='Only Include Opiods?', widget=forms.CheckboxInput(attrs={'style': 'margin-left: 10px;'}))

