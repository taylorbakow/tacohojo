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

@view_function
def process_request(request):
    prescribers = hmod.Prescriber.objects.all()

    context={
        'prescribers': prescribers,
    }

    return request.dmp.render('managedata.html', context)

view_function
def create(request):
    return process_request(request)