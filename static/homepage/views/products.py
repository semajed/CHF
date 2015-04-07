from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.contrib.auth.decorators import permission_required,user_passes_test
import homepage.models as hmod

templater = get_renderer('homepage')

################### USER PAGE ###########################
@view_function
# @permission_required('product.add_product', login_url='/homepage/login/')
@user_passes_test(lambda u: u.groups.filter(name="Manager") or u.is_superuser,login_url='/homepage/login/')
def process_request(request):
	params={}

	try:
		params['products'] = hmod.Product.objects.all()
	except hmod.Product.DoesNotExist:
		raise e

	try:
		user = hmod.User.objects.filter(username = "don't choose me").delete()
	except hmod.User.DoesNotExist:
		pass

	try:
		event = hmod.Address.objects.filter(city = "delete me").delete()
	except hmod.User.DoesNotExist:
		pass


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
		})
	if request.method == 'POST':
		form = ProductEditForm(request.POST)
		if form.is_valid():
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']
			product.category = form.cleaned_data['category']
			product.currentPrice = form.cleaned_data['currentPrice']
			# product.owner = form.cleaned_data['owner']
			product.save()
			return HttpResponseRedirect('/homepage/products')

	#delete spaceholder users


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
	# owner = forms.ModelChoiceField(
	# 	required=True,
	# 	queryset=hmod.User.objects.exclude(username = "don't choose me"),
	# 	widget=forms.Select(attrs={'class': 'form-control'}))

	def clean_name(self):
		if len(self.cleaned_data['name']) < 3:
			raise forms.ValidationError("Name of event must be longer than 3 characters")
		return self.cleaned_data['name']

	# def clean_name(self):
	# 	price = self.cleaned_data['currentPrice']
	# 	if price < 0.00:
	# 		raise forms.ValidationError("Price must be greater than $0.00")
	# 	return self.cleaned_data['currentPrice']

################### CREATE ITEM ###########################
@view_function
def create(request):
	params={}

	address = hmod.Address()
	address.city = "delete me"
	address.save()

	user = hmod.User()
	user.username = "don't choose me"
	user.address = address
	user.save()

	product1 = hmod.Product()
	product1.name = ""
	product1.currentPrice = 0.00
	# product1.owner = user
	product1.save()
	user.save()


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






