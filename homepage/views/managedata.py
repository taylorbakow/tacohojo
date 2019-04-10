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
def process_request(request, prescriber:hmod.Prescriber):
    return request.dmp.render('managedata.html')

@view_function
def create(request, pid:hmod.Prescriber):
    return process_request(request)

@view_function
def remove(request, pid:hmod.Prescriber):
    return process_request(request)

@view_function
def edit(request, pid:hmod.Prescriber):
    return process_request(request)