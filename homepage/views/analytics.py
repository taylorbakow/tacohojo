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
        if request.user.groups.filter(name='Health Officials').exists() or request.user.groups.filter(name='Prescribers').exists():
            return request.dmp.render('analytics.html')
        else:
            return HttpResponseRedirect('/homepage/index')
    else:
        return HttpResponseRedirect('/account/login')