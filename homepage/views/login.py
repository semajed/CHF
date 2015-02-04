from django.conf import settings
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetime import datetime
import homepage.models as hmod
from django import forms

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params={}

	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/homepage/users/')


	params['form'] = form
	return templater.render_to_response(request, 'login.html', params)

class LoginForm(forms.Form):
	username = forms.CharField(
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(
		required="True",
		label="Password",
		widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	def clean(self):
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		if user == None:
			raise forms.ValidationError("You shall not pass!")
		return self.cleaned_data
