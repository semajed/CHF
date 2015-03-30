from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required, user_passes_test

import homepage.models as hmod

templater = get_renderer('homepage')

################### USER PAGE ###########################
@view_function
@permission_required('auth_permission.change_permission', login_url='/homepage/login/')
def process_request(request):
	params={}

	try:
		params['users'] = hmod.User.objects.all().order_by('last_name','first_name')
	except hmod.User.DoesNotExist:
		raise e

	return templater.render_to_response(request, 'permissions.html', params)

################### EDIT USER ###########################
@view_function
def edit(request):
	params={}

	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
		address = hmod.Address.objects.get(id=user.address.id)
	except hmod.User.DoesNotExist:
		raise HttpResponseRedirect('homepage/permissions/')
	
	form = UserEditForm(initial={
		'is_superuser': user.is_superuser,
		'is_staff': user.is_staff,
		})
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		if form.is_valid():
			user.is_superuser = form.cleaned_data['is_superuser']
			user.is_staff = form.cleaned_data['is_staff']

			#put in admin group
			if user.is_superuser == True:
				user.groups.clear()
				adminGroup = Group.objects.get(name='Admin')
				user.groups.add(adminGroup)
			if user.is_superuser == False:
				adminGroup = Group.objects.get(name='Admin')
				user.groups.remove(adminGroup)
				
			#put in manager group
			if user.is_staff == True:
				user.groups.clear()
				managerGroup = Group.objects.get(name='Manager')
				user.groups.add(managerGroup)
			if user.is_staff == False:
				managerGroup = Group.objects.get(name='Manager')
				user.groups.remove(managerGroup)
			#remove all groups
			if user.is_staff == False & user.is_superuser == False:
				user.groups.clear()
			user.save()
			
			return HttpResponseRedirect('/homepage/permissions')

	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'permissions.edit.html', params)

class UserEditForm(forms.Form):
	is_superuser = forms.BooleanField(
		label="Admin:",
		required=False)
	is_staff = forms.BooleanField(
		label="Manager:",
		required=False)


