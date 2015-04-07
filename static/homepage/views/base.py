from django.conf import settings
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO



templater = get_renderer('homepage')


@view_function
def process_request(request):
    params={}


    print(">>>>>>>>>>> BASE PROCESS REQUEST")
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']

            s = Server(
                'www.mycolonialfoundation.org',
                port=8889,
                get_info=GET_ALL_INFO)
            
            print(">>>>>>>>>>>>>>>>>>",s)

            c = Connection(s, 
                auto_bind = True, 
                client_strategy = STRATEGY_SYNC,
                user = un + '@mycolonialfoundation.local',
                password='Password1',
                authentication=AUTH_SIMPLE)

            print(">>>>>>>>>>>>>>",c)

            if c:
                try:
                    u = hmod.User.objects.get(username=un)
                except hmod.User.DoesNotExist:
                    u.username = un
                    u.first_name = ''
                    u.last_name = ''
                    u.email = ''
                    u.set_password(pw)
                    u.save()

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
        print(">>>>>>>>>>> BASE LOGINFORM")
        if form.is_valid():

            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']

            s = Server(
                'www.mycolonialfoundation.org',
                port=8889,
                get_info=GET_ALL_INFO)
            
            print(">>>>>>>>>>>>>>>>>>",s)

            c = Connection(s, 
                auto_bind = True, 
                client_strategy = STRATEGY_SYNC,
                user = un + '@mycolonialfoundation.local',
                password='Password1',
                authentication=AUTH_SIMPLE)

            print(">>>>>>>>>>>>>>",c)

            if c:
                try:
                    u = hmod.User.objects.get(username=un)
                except hmod.User.DoesNotExist:
                    u.username = un
                    u.first_name = ''
                    u.last_name = ''
                    u.email = ''
                    u.set_password(pw)
                    u.save()

                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
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

@view_function
def forgot_password(request):
    params={}

    form = forgot_password_form()
    if request.method == 'POST':
        form = forgot_password_form(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username']
                )

            return HttpResponseRedirect('/homepage/forgot_password/')

    params['form'] = form
    return templater.render_to_response(request, 'index.loginform.html', params)

class forgot_password_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        user = authenticate(username=self.cleaned_data['username'])
        if user == None:
          raise forms.ValidationError('Sorry! Incorrect username or password.')
        return self.cleaned_data









