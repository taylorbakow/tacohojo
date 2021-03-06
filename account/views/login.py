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

    if request.method == 'POST':
        
        form = loginForm(request.POST)
        
        if form.is_valid():
           user = authenticate(username=request.POST['Username'], password=request.POST['Password'])
           user = amod.User.objects.get(username=request.POST['Username'])
           login(request, user)
           return HttpResponseRedirect('/homepage/index', user)
        else:
           forms.ValidationError("Invalid Credentials")
    else:
        form = loginForm()

    context = {
        'form': form,
    }   
    return request.dmp.render('login.html', context)


class loginForm(forms.Form):
   Username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'control'}))
   Password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'control'}))

   def clean(self):
       user = authenticate(username=self.cleaned_data['Username'], password=self.cleaned_data['Password'])
       if user is None:
           raise forms.ValidationError('Invalid Username or Password.')
       return self.cleaned_data