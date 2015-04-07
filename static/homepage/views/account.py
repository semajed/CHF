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
def process_request(request):
    params={}

    try:
        user = hmod.User.objects.get(id=request.urlparams[0])
        address = hmod.Address.objects.get(id=user.address.id)
        photo = hmod.Photograph.objects.get(id=user.photo.id)
    except hmod.User.DoesNotExist:
        raise HttpResponseRedirect('homepage/index/')

    params['user'] = user
    params['address'] = address
    params['photo'] = photo
    return templater.render_to_response(request, 'account.html', params)











