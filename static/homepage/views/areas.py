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
# @permission_required('areas.add_area', login_url='/homepage/login/')
@user_passes_test(lambda u: u.groups.filter(name="Manager") or u.is_superuser,login_url='/homepage/login/')
def process_request(request):
	params={}

	try:
		params['areas'] = hmod.Area.objects.all()
	except hmod.Area.DoesNotExist:
		raise e

	try:
		event = hmod.Event.objects.filter(name = "do no select me").delete()
	except hmod.User.DoesNotExist:
		pass

	return templater.render_to_response(request, 'areas.html', params)

################### EDIT USER ###########################
@view_function
def edit(request):
	params={}

	try:
		area = hmod.Area.objects.get(id=request.urlparams[0])
	except hmod.Area.DoesNotExist:
		raise HttpResponseRedirect('homepage/areas/')
	
	form = AreaEditForm(initial={
		'name': area.name,
		'description': area.description,
		'placeNumber': area.placeNumber,
		'event': area.event
		})
	if request.method == 'POST':
		form = AreaEditForm(request.POST)
		if form.is_valid():
			area.name = form.cleaned_data['name']
			area.description = form.cleaned_data['description']
			area.placeNumber = form.cleaned_data['placeNumber']
			area.event = form.cleaned_data['event']
			area.save()

			return HttpResponseRedirect('/homepage/areas')


	params['form'] = form
	params['area'] = area
	return templater.render_to_response(request, 'areas.edit.html', params)

class AreaEditForm(forms.Form):
	name = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	placeNumber = forms.IntegerField(
		required=True,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	event = forms.ModelChoiceField(
		required=True,
		queryset=hmod.Event.objects.exclude(name = "do no select me"),
		widget=forms.Select(attrs={'class': 'form-control'}))

	def clean_name(self):
		if len(self.cleaned_data['name']) < 5:
			raise forms.ValidationError("Name of the area needs to be 5 characters or longer")
		return self.cleaned_data['name']


################### CREATE ITEM ###########################
@view_function
def create(request):
	params={}

	event1 = hmod.Event()
	event1.name = "do no select me"
	event1.startDate = datetime.now()
	event1.endDate = datetime.now()
	event1.save()

	area = hmod.Area()
	area.name = ""
	area.description = ""
	area.placeNumber = 0
	area.event = event1
	area.save()


	return HttpResponseRedirect('/homepage/areas.edit/{}/'.format(area.id))

#################### DELETE ITEM ###########################
@view_function
def delete(request):
	params={}
	
	try:
		area = hmod.Area.objects.get(id=request.urlparams[0])
	except hmod.Area.DoesNotExist:
		return HttpResponseRedirect('/homepage/areas/')

	area.delete()

	return HttpResponseRedirect('/homepage/areas/')









