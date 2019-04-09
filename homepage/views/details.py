from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from decimal import Decimal
from homepage import models as hmod
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

@view_function
def process_request(request, prescriber:hmod.Prescriber):
    return request.dmp.render('prescriberdetail.html')


@view_function
def drugdetail(request, drugid:hmod.Opioids):

    drug = hmod.Drugs_Details.objects.filter(DrugID=drugid).first()
    prescribers = hmod.Drugs_Details.objects.order_by('-QtyPrescribed').filter(DrugID=drugid)[0:10]

    context={
        'drug': drug,
        'prescribers': prescribers,
    }
    return request.dmp.render('drugdetail.html', context)