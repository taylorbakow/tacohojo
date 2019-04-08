from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms
from account import models as amod
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import django.contrib.auth


@view_function
def process_request(request):
    # log the user out
    logout(request)
    # 
    return HttpResponseRedirect('/account/login/')