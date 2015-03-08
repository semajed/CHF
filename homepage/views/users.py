from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required,user_passes_test
import homepage.models as hmod
from django.core.files import File
from django.contrib.auth import authenticate, login, logout

templater = get_renderer('homepage')

################### USER PAGE ###########################
@view_function
# @permission_required('users.add_user', login_url='/homepage/login/')
@user_passes_test(lambda u: u.groups.filter(name="Manager") or u.is_superuser,login_url='/homepage/login/')
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
		address = hmod.Address.objects.get(id=user.address.id)
		photo = hmod.Photograph.objects.get(id=user.photo.id)
	except hmod.User.DoesNotExist:
		raise HttpResponseRedirect('homepage/users/')
	
	form = UserEditForm1(initial={
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'phoneNumber': user.phoneNumber,
		'street1': address.street1,
		'street2': address.street2,
		'city': address.city,
		'state': address.state,
		'ZIP': address.ZIP,
		'secQuestion': user.secQuestion,
		'secAnswer': user.secAnswer,
		'emergencyContactPhone': user.emergencyContactPhone,
		'emergencyContactRelation': user.emergencyContactRelation,
		'biographicalSketch': user.biographicalSketch,
		'organizationName': user.organizationName,
		'photo': photo.image
		})
	
	if request.method == 'POST':
		form = UserEditForm1(request.POST, request.FILES)
		form.userid = user.id
		
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.phoneNumber = form.cleaned_data['phoneNumber']
			address.street1 = form.cleaned_data['street1']
			address.street2 = form.cleaned_data['street2']
			address.city = form.cleaned_data['city']
			address.state = form.cleaned_data['state']
			address.ZIP = form.cleaned_data['ZIP']
			user.secQuestion = form.cleaned_data['secQuestion']
			user.secAnswer = form.cleaned_data['secAnswer']
			user.emergencyContactPhone = form.cleaned_data['emergencyContactPhone']
			user.emergencyContactRelation = form.cleaned_data['emergencyContactRelation']
			user.biographicalSketch = form.cleaned_data['biographicalSketch']
			user.organizationName = form.cleaned_data['organizationName']
			photo.image = form.cleaned_data['photo']
			photo.save()
			address.save()
			user.save()

			return HttpResponseRedirect('/homepage/index')


	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'users.edit.html', params)

class UserEditForm1(forms.Form):
	username = forms.CharField(
		label="Username:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(
		label="First Name:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(
		label="Last Name:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	phoneNumber = forms.CharField(
		label="Phone:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(
		label="Email:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	street1 = forms.CharField(
		label="Street 1:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	street2 = forms.CharField(
		label="Street 2:",
		required=False,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	city = forms.CharField(
		label="City:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	state = forms.CharField(
		label="State:",
		required=True,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	ZIP = forms.CharField(
		label="ZIP:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
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
	emergencyContactPhone = forms.CharField(
		label="Emergency Phone Number:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	emergencyContactRelation = forms.CharField(
		label="Emergency Contact Relation:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	biographicalSketch = forms.CharField(
		label="Biographical Sketch:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.Textarea(attrs={'class': 'form-control'}))
	organizationName = forms.CharField(
		label="Organization Name:",
		required=False,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	photo = forms.ImageField(
		label="Upload Image:",
		required=True,)


	def clean_username(self):
		user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
		if user_count >= 1:	
			raise forms.ValidationError("This user name is already taken bro")
		return self.cleaned_data['username']

	def clean_ZIP(self):
		if len(self.cleaned_data['ZIP']) < 5:
			raise forms.ValidationError("Zip code must contain at least 5 digits")
		return self.cleaned_data['ZIP']

	# def clean_password(self):
	# 	if self.cleaned_data['password'] != self.cleaned_data['password2']:
	# 		raise forms.ValidationError("You typed in two different passwords")
	# 	return self.cleaned_data['password']


################### CREATE USER ###########################
@view_function
def create(request):
	params={}
	address1 = hmod.Address()
	address1.save()

	photo = hmod.Photograph()
	photo.dateTaken = "1999-02-03"
	photo.placeTaken = "Mt. Olympus"
	photo.save()

	user1 = hmod.User()
	user1.address = address1
	user1.photo = photo
	user1.save()

	group = Group.objects.get(name='User')
	user1.groups.add(group)

	return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user1.id))


################### EDIT USER ###########################
@view_function
def userEdit(request):
	params={}

	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
		address = hmod.Address.objects.get(id=user.address.id)
		photo = hmod.Photograph.objects.get(id=user.photo.id)
	except hmod.User.DoesNotExist:
		raise HttpResponseRedirect('homepage/users/')
	
	form = UserEditForm2(initial={
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		'phoneNumber': user.phoneNumber,
		'street1': address.street1,
		'street2': address.street2,
		'city': address.city,
		'state': address.state,
		'ZIP': address.ZIP,
		'secQuestion': user.secQuestion,
		'secAnswer': user.secAnswer,
		'emergencyContactPhone': user.emergencyContactPhone,
		'emergencyContactRelation': user.emergencyContactRelation,
		'biographicalSketch': user.biographicalSketch,
		'organizationName': user.organizationName,
		'photo':photo.image
		})
	if request.method == 'POST':
		form = UserEditForm2(request.POST, request.FILES)
		form.userid = user.id
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.phoneNumber = form.cleaned_data['phoneNumber']
			address.street1 = form.cleaned_data['street1']
			address.street2 = form.cleaned_data['street2']
			address.city = form.cleaned_data['city']
			address.state = form.cleaned_data['state']
			address.ZIP = form.cleaned_data['ZIP']
			user.set_password(form.cleaned_data['password'])
			user.secQuestion = form.cleaned_data['secQuestion']
			user.secAnswer = form.cleaned_data['secAnswer']
			user.emergencyContactPhone = form.cleaned_data['emergencyContactPhone']
			user.emergencyContactRelation = form.cleaned_data['emergencyContactRelation']
			user.biographicalSketch = form.cleaned_data['biographicalSketch']
			user.organizationName = form.cleaned_data['organizationName']
			photo.image = form.cleaned_data['photo']
			user.photo.save()
			address.save()
			user.save()
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request,user)

			return HttpResponseRedirect('/homepage/index')


	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'users.edit.html', params)

class UserEditForm2(forms.Form):
	username = forms.CharField(
		label="Username:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(
		label="First Name:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(
		label="Last Name:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	phoneNumber = forms.CharField(
		label="Phone:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(
		label="Email:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	street1 = forms.CharField(
		label="Street 1:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	street2 = forms.CharField(
		label="Street 2:",
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	city = forms.CharField(
		label="City:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	state = forms.CharField(
		label="State:",
		required=True,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	ZIP = forms.CharField(
		label="ZIP:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(
		label="Password:",
		required=True,
		min_length=1,
		max_length=200,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(
		label="Re-type Password:",
		min_length=1,
		max_length=200,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
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
	emergencyContactPhone = forms.CharField(
		label="Emergency Phone Number:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	emergencyContactRelation = forms.CharField(
		label="Emergency Contact Relation:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	biographicalSketch = forms.CharField(
		label="Biographical Sketch:",
		required=True,
		min_length=1,
		max_length=700,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	organizationName = forms.CharField(
		label="Organization Name:",
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	photo = forms.ImageField(
		label="Upload Image:",
		required=True,)


	def clean_username(self):
		user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
		if user_count >= 1:	
			raise forms.ValidationError("This user name is already taken bro")
		return self.cleaned_data['username']

	def clean_ZIP(self):
		if len(self.cleaned_data['ZIP']) < 5:
			raise forms.ValidationError("Zip code must contain at least 5 digits")
		return self.cleaned_data['ZIP']

	# def clean_password(self):
	# 	if self.cleaned_data['password'] != self.cleaned_data['password2']:
	# 		raise forms.ValidationError("You typed in two different passwords")
	# 	return self.cleaned_data['password']



################### CREATE USER ###########################
@view_function
def userCreate(request):
	params={}
	address1 = hmod.Address()
	address1.save()

	photo = hmod.Photograph()
	photo.dateTaken = "1999-02-03"
	photo.placeTaken = "Mt. Olympus"
	photo.save()

	user1 = hmod.User()
	user1.address = address1
	user1.photo = photo
	user1.save()

	group = Group.objects.get(name='User')
	user1.groups.add(group)

	return HttpResponseRedirect('/homepage/users.userEdit/{}/'.format(user1.id))


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












