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
                pList = hmod.Prescriber.objects.filter( Q(Fname__icontains=pname) | Q(Lname__icontains=pname)).distinct()[0:10]
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
                pList = hmod.Prescriber.objects.filter( Q(Fname__icontains=pname) | Q(Lname__icontains=pname)).distinct()[0:10]
                objectType = 'Prescriber'
            elif len(request.POST['drugname']) > 0:
                print('drug')
                dname = request.POST['drugname']
                dList = hmod.Opioids.objects.filter(DrugName__icontains=dname).distinct()[0:10]
                objectType = 'Drug'
        else:
            pass

        group = request.user.groups.first()
        context = {
            'formP': formP,
            'formD': formD,
            'pList': pList,
            'dList': dList,
            'objectType': objectType,
            'ddList': ddList,
            'group': group
        }
        return request.dmp.render('index.html', context)
    else:
        return HttpResponseRedirect('/account/login')

class PrescriberForm(forms.Form):
    prescribername = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Prescriber', 'placeholder' :'Search by Prescriber'}), required=False)

class DrugForm(forms.Form):
    drugname = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Drug', 'placeholder' :'Search by Drug Name'}), required=False)

