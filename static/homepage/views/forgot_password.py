from django.conf import settings
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
import homepage.models as hmod
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}

    form = forgot_password_form()
    if request.method == 'POST':
        form = forgot_password_form(request.POST)
        if form.is_valid():
            gotUser = False
            try:
                user = hmod.User.objects.get(username=form.cleaned_data['username'])
                params['user'] = user
                gotUser = True
            except hmod.User.DoesNotExist:
                gotUser = False
                HttpResponseRedirect("/homepage/index/")
            
            # gotUser = True
            # params['gotUser'] = gotUser
            if gotUser is True:
                return HttpResponseRedirect('/homepage/forgot_password.check_security/{}'.format(user.id))
            else:
                HttpResponseRedirect("/homepage/index/")
    gotUser = False
    params['gotUser'] = gotUser
    params['form'] = form
    return templater.render_to_response(request, 'forgot_password.html', params)

class forgot_password_form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

@view_function
def check_security(request):
    params = {}
    userid = request.urlparams[0]

    try:
        user = hmod.User.objects.get(id=userid)
        params['user'] = user
        gotUser = True
    except hmod.User.DoesNotExist:
        raise e
    
    params['gotUser'] = gotUser

    form = security_form()
    if request.method == 'POST':
        form = security_form(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['security_answer']
            if answer == user.secAnswer:

                params2 = {}
                subject = "Reset Password"
                #set exp date
                user.exp_date = datetime.now() + timedelta(days=1)
                #set random string
                user.forgot_password_code = get_random_string(length=24)
                user.save()
                params2['user'] = user

                message = templater.render(request, 'email_temp_pass.html', params2)
                from_email = "mycolonialfoundation@gmail.com"
                to_email = user.email
                send_mail(subject, message, from_email,[to_email],html_message=message,fail_silently=False)

            else:
                print(">>>>>>>>>> BAD ANSWER")

            return HttpResponseRedirect('/homepage/forgot_password/')

    params['form'] = form
    return templater.render_to_response(request, 'forgot_password.html', params)

class security_form(forms.Form):
    security_answer = forms.CharField(
        label="Security Answer:",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(label=_("Email"), max_length=254)

#     def save(self, domain_override=None,
#              subject_template_name='registration/password_reset_subject.txt',
#              email_template_name='registration/password_reset_email.html',
#              use_https=False, token_generator=default_token_generator,
#              from_email=None, request=None):
#         """
#         Generates a one-use only link for resetting password and sends to the
#         user.
#         """
#         from django.core.mail import send_mail
#         UserModel = get_user_model()
#         email = self.cleaned_data["email"]
#         active_users = UserModel._default_manager.filter(
#             email__iexact=email, is_active=True)
#         for user in active_users:
#             # Make sure that no email is sent to a user that actually has
#             # a password marked as unusable
#             if not user.has_usable_password():
#                 continue
#             if not domain_override:
#                 current_site = get_current_site(request)
#                 site_name = current_site.name
#                 domain = current_site.domain
#             else:
#                 site_name = domain = domain_override
#             c = {
#                 'email': user.email,
#                 'domain': domain,
#                 'site_name': site_name,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'user': user,
#                 'token': token_generator.make_token(user),
#                 'protocol': 'https' if use_https else 'http',
#             }
#             subject = loader.render_to_string(subject_template_name, c)
#             # Email subject *must not* contain newlines
#             subject = ''.join(subject.splitlines())
#             email = loader.render_to_string(email_template_name, c)
#             send_mail(subject, email, from_email, [user.email])














