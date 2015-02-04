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
		params['products'] = hmod.Product.objects.all()
	except hmod.Product.DoesNotExist:
		raise e

	return templater.render_to_response(request, 'products.html', params)

################### EDIT USER ###########################
@view_function
def edit(request):
	params={}

	try:
		product = hmod.Product.objects.get(id=request.urlparams[0])
	except hmod.Product.DoesNotExist:
		raise HttpResponseRedirect('homepage/products/')
	
	form = ProductEditForm(initial={
		'name': product.name,
		'description': product.description,
		'category': product.category,
		'currentPrice': product.currentPrice,
		'person': product.person.name,
		})
	if request.method == 'POST':
		form = ProductEditForm(request.POST)
		if form.is_valid():
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']
			product.category = form.cleaned_data['category']
			product.currentPrice = form.cleaned_data['currentPrice']
			product.person.name = form.cleaned_data['person']
			product.save()

			return HttpResponseRedirect('/homepage/products')


	params['form'] = form
	params['product'] = product
	return templater.render_to_response(request, 'products.edit.html', params)

class ProductEditForm(forms.Form):
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
	category = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	currentPrice = forms.DecimalField(
		required=True,
		max_digits=6,
		decimal_places=2,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	person = forms.CharField(
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

	product1 = hmod.Product()
	product1.name = ""
	product1.description = ""
	product1.category = ""
	product1.currentPrice = 0.00
	product1.person = person1
	product1.save()


	return HttpResponseRedirect('/homepage/products.edit/{}/'.format(product1.id))

################### DELETE ITEM ###########################
@view_function
def delete(request):
	params={}
	
	try:
		product = hmod.Product.objects.get(id=request.urlparams[0])
	except hmod.Product.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')

	product.delete()

	return HttpResponseRedirect('/homepage/products/')






