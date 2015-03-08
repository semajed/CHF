from django.conf import settings
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User



templater = get_renderer('homepage')

@view_function
def process_request(request):
    params={}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form
    return templater.render_to_response(request, 'index.html', params)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user == None:
          raise forms.ValidationError('Sorry! Incorrect username or password.')
        return self.cleaned_data

@view_function
def loginform(request):
    params={}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
                )
            login(request, user)

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
            ''')

    params['form'] = form
    return templater.render_to_response(request, 'index.loginform.html', params)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user == None:
          raise forms.ValidationError('Sorry! Incorrect username or password.')
        return self.cleaned_data

@view_function
def logout_view(request):
  logout(request)

  return HttpResponseRedirect('/homepage/index')









  