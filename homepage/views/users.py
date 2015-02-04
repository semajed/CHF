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
		params['users'] = hmod.User.objects.all().order_by('last_name','first_name')
	except hmod.User.DoesNotExist:
		raise e

	return templater.render_to_response(request, 'users.html', params)


################### EDIT USER ###########################
@view_function
def edit(request):
	params={}

	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		raise HttpResponseRedirect('homepage/users/')
	
	form = UserEditForm(initial={
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		})
	if request.method == 'POST':
		form = UserEditForm(request.POST)
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.save()

			return HttpResponseRedirect('/homepage/users')


	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'users.edit.html', params)

class UserEditForm(forms.Form):
	username = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(
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

################### CREATE USER ###########################
@view_function
def create(request):
	params={}

	person1 = hmod.Person()
	person1.save()

	user1 = hmod.User()
	user1.username = ""
	user1.first_name = ""
	user1.last_name = ""
	user1.owner = person1
	user1.save()

	return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user1.id))


################### DELETE USER ###########################
@view_function
def delete(request):
	params={}
	
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/users/')

	user.delete()

	return HttpResponseRedirect('/homepage/users/')












