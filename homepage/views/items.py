from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
import homepage.models as hmod

templater = get_renderer('homepage')

################### ITEM PAGE ###########################
@view_function
def process_request(request):
	params={}

	try:
		params['items'] = hmod.Item.objects.all()
	except hmod.Item.DoesNotExist:
		raise e

	return templater.render_to_response(request, 'items.html', params)

################### EDIT ITEM ###########################
@view_function
def edit(request):
	params={}

	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		raise HttpResponseRedirect('homepage/items/')
	
	form = ItemEditForm(initial={
		'name': item.name,
		'description': item.description,
		'value': item.value,
		'STP': item.STP,
		'owner': item.owner.name,
		})

	if request.method == 'POST':
		form = ItemEditForm(request.POST)
		if form.is_valid():
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.STP = form.cleaned_data['STP']
			item.owner.name = form.cleaned_data['owner']
			item.save()

			return HttpResponseRedirect('/homepage/items')


	params['form'] = form
	params['item'] = item
	return templater.render_to_response(request, 'items.edit.html', params)

class ItemEditForm(forms.Form):
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
	value = forms.DecimalField(
		required=True,
		max_digits=6,
		decimal_places=2,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	STP = forms.DecimalField(
		required=True,
		max_digits=6,
		decimal_places=2,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	owner = forms.CharField(
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

	person1 = hmod.Person()
	person1.name = ""
	person1.save()

	item1 = hmod.Item()
	item1.name = ""
	item1.description = ""
	item1.value = 0.00
	item1.STP = 0.00
	item1.owner = person1
	item1.save()


	return HttpResponseRedirect('/homepage/items.edit/{}/'.format(item1.id))

################### DELETE ITEM ###########################
@view_function
def delete(request):
	params={}
	
	try:
		item = hmod.Item.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')

	item.delete()

	return HttpResponseRedirect('/homepage/items/')












