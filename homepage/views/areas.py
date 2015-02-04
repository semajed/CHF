from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
import homepage.models as hmod

templater = get_renderer('homepage')

################### USER PAGE ###########################
@view_function
def process_request(request):
	params={}

	try:
		params['areas'] = hmod.Area.objects.all()
	except hmod.Area.DoesNotExist:
		raise e

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
		'event': area.event.name,
		})
	if request.method == 'POST':
		form = AreaEditForm(request.POST)
		if form.is_valid():
			area.name = form.cleaned_data['name']
			area.description = form.cleaned_data['description']
			area.placeNumber = form.cleaned_data['placeNumber']
			area.event.name = form.cleaned_data['event']
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
	event = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	# def clean_empname(self):
	# 	if len(self.cleaned_data['first_name']) < 5:
	# 		raise forms.ValidationError("Hey man, fix it")
	# 	try:
	# 		emp = hmod.User.objects.get(firstName=self.cleaned_data['firstName'])
	# 		raise forms.ValidationError("This user name is already taken bro")
	# 	except hmod.Employee.DoesNotExist:
	# 		pass # we want this!

################### CREATE ITEM ###########################
@view_function
def create(request):
	params={}

	event1 = hmod.Event()

	event1.name = "from area"
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









