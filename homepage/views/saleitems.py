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
		params['saleitems'] = hmod.SaleItem.objects.all()
	except hmod.SaleItem.DoesNotExist:
		raise e

	return templater.render_to_response(request, 'saleitems.html', params)

################### EDIT USER ###########################
@view_function
def edit(request):
	params={}

	try:
		saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
	except hmod.SaleItem.DoesNotExist:
		raise HttpResponseRedirect('homepage/saleitems/')
	
	form = SaleItemEditForm(initial={
		'name': saleitem.name,
		'description': saleitem.description,
		'lowPrice': saleitem.lowPrice,
		'highPrice': saleitem.highPrice,
		'area': saleitem.area.name,
		})
	if request.method == 'POST':
		form = SaleItemEditForm(request.POST)
		if form.is_valid():
			saleitem.name = form.cleaned_data['name']
			saleitem.description = form.cleaned_data['description']
			saleitem.lowPrice = form.cleaned_data['lowPrice']
			saleitem.highPrice = form.cleaned_data['highPrice']
			saleitem.area.name = form.cleaned_data['area']
			saleitem.save()

			return HttpResponseRedirect('/homepage/saleitems')


	params['form'] = form
	params['saleitem'] = saleitem
	return templater.render_to_response(request, 'saleitems.edit.html', params)

class SaleItemEditForm(forms.Form):
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
	lowPrice = forms.DecimalField(
		required=True,
		max_digits=6,
		decimal_places=2,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	highPrice = forms.DecimalField(
		required=True,
		max_digits=6,
		decimal_places=2,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	area = forms.CharField(
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

	event1.name = ""
	event1.startDate = datetime.now()
	event1.endDate = datetime.now()
	event1.save()

	area = hmod.Area()
	area.name = ""
	area.description = "d"
	area.placeNumber = 0
	area.event = event1
	area.save()

	saleitem = hmod.SaleItem()
	saleitem.name = ""
	saleitem.description = ""
	saleitem.lowPrice = 0.00
	saleitem.highPrice = 0.00
	saleitem.area = area
	saleitem.save()

	return HttpResponseRedirect('/homepage/saleitems.edit/{}/'.format(saleitem.id))

#################### DELETE ITEM ###########################
@view_function
def delete(request):
	params={}
	
	try:
		saleitem = hmod.SaleItem.objects.get(id=request.urlparams[0])
	except hmod.SaleItem.DoesNotExist:
		return HttpResponseRedirect('/homepage/saleitems/')

	saleitem.delete()

	return HttpResponseRedirect('/homepage/saleitems/')









