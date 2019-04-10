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
    prescribername = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'name': 'Prescriber', 'placeholder' :'Search by Prescriber'}), required=False)

view_function
def create(request):
    return process_request(request)