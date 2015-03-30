from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from django.shortcuts import render_to_response
from django.contrib import auth
from datetime import datetime
from django import forms
from django.contrib.auth.decorators import permission_required,user_passes_test
import homepage.models as hmod

templater = get_renderer('homepage')

################### USER PAGE ###########################
@view_function
def edit(request):
    params={}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
    except hmod.User.DoesNotExist:
        raise HttpResponseRedirect('homepage/index/')

    form = UserEditForm1(initial={
        'password': user.password,
        'secQuestion': user.secQuestion,
        'secAnswer': user.secAnswer,
        })
    if request.method == 'POST':
        form = UserEditForm1(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.secQuestion = form.cleaned_data['secQuestion']
            user.secAnswer = form.cleaned_data['secAnswer']
            user.save()

            return HttpResponseRedirect('/homepage/index/')


    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'accountSecurity.edit.html', params)

class UserEditForm1(forms.Form):
    password = forms.CharField(
        label="Password:",
        required=True,
        min_length=1,
        max_length=200,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    secQuestion = forms.CharField(
        label="Security Question:",
        required=True,
        min_length=1,
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    secAnswer = forms.CharField(
        label="Security Answer:",
        required=True,
        min_length=1,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))











