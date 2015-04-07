from django.conf import settings
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO



templater = get_renderer('homepage')

@view_function
def process_request(request):
    params={}

    return templater.render_to_response(request, 'index.html', params)



@view_function
def loginform(request):
    params={}

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = None
            print(">>>>>>>>>>>>>FORM IS VALID")
            try:
                user = hmod.User.objects.get(username=un)
                print(">>>>>>>>>>>>>BEFORE THE LOGIN",user)
            except hmod.User.DoesNotExist:
                pass
            
            if user != None:
                print(">>>>>>>>>>>>>FOUND THE USER")
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, user)
            else:
                print(">>>>>>>>>>>>>LDAP GAMES")
                s = Server(
                    'www.mycolonialfoundation.org',
                    port=8889,
                    get_info=GET_ALL_INFO)
                

                c = Connection(s, 
                    auto_bind = True, 
                    client_strategy = STRATEGY_SYNC,
                    user = un + '@mycolonialfoundation.local',
                    password='Password1',
                    authentication=AUTH_SIMPLE)


                if c:
                    try:
                        u = hmod.User.objects.get(username=un)
                    except hmod.User.DoesNotExist:
                        params={}
                        a = hmod.Address()
                        a.save()

                        photo = hmod.Photograph()
                        photo.dateTaken = "1999-02-03"
                        photo.placeTaken = "Mt. Olympus"
                        photo.save()

                        u = hmod.User()
                        u.username = un
                        u.first_name = un
                        u.last_name = ''
                        u.email = ''
                        u.address = a
                        u.photo = photo
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

    # def clean(self):
    #     user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    #     if user == None:
    #       raise forms.ValidationError('Sorry! Incorrect username or password.')
    #     return self.cleaned_data

@view_function
def logout_view(request):
  logout(request)

  return HttpResponseRedirect('/homepage/index')










  