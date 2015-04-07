from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime, timedelta
from django.utils import formats
from django.contrib.auth.decorators import permission_required, user_passes_test
import homepage.models as hmod
from django.utils import timezone
from django.core.mail import send_mail


templater = get_renderer('homepage')

################### GET ALL RENTALS ###########################
@view_function
# @permission_required('events.add_event', login_url='/homepage/login/')
@user_passes_test(lambda u: u.groups.filter(name="Manager") or u.is_superuser,login_url='/homepage/login/')
def process_request(request):
    params={}

    lates = False
    params['lates'] = lates

    try:
        params['rentals'] = hmod.Rental.objects.all()
    except hmod.Event.DoesNotExist:
        raise HttpResponseRedirect('/homepage/index/')

    return templater.render_to_response(request, 'rentals.html', params)

################### GET LATE RENTALS ###########################
@view_function
def late(request):
    params={}

    lates = True
    params['lates'] = lates
    
    now = datetime.now()
    thirty = timezone.now() - timedelta(days=30)
    sixty = timezone.now() - timedelta(days=60)
    ninety = timezone.now() - timedelta(days=90)

    try:
        params['today_to_thirty'] = hmod.Rental.objects.filter(dueDate__lte=now,dueDate__gt=thirty).order_by('dueDate')
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    try:
        params['thirty_to_sixty'] = hmod.Rental.objects.filter(dueDate__lte=thirty,dueDate__gt=sixty).order_by('dueDate')
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    try:
        params['sixty_to_ninety'] = hmod.Rental.objects.filter(dueDate__lte=sixty,dueDate__gt=ninety).order_by('dueDate')
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    try:
        params['ninety_plus'] = hmod.Rental.objects.filter(dueDate__lte=ninety).order_by('dueDate')
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    return templater.render_to_response(request, 'rentals.html', params)

################### RETURN RENTAL ###########################
@view_function
def rental_return(request):
    params={}
    rented_items = []
    now = datetime.now()
    try:
        rental = hmod.Rental.objects.get(id=request.urlparams[0])
        rented_items = hmod.RentedItem.objects.filter(rental_id=rental.id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    rental_return = hmod.Return()
    

    form = fee_form(initial={
        'damageFee': 0.00,
        'lateFee': 0.00,
        'totalFee': 0.00,
        })
    if request.method == 'POST':
        form = fee_form(request.POST)
        if form.is_valid():
            rental_return.damageFee = form.cleaned_data['damageFee']
            rental_return.lateFee = form.cleaned_data['lateFee']
            rental_return.totalFee = form.cleaned_data['totalFee']
            rental_return.returnTime = datetime.now()
            rental_return.user = request.user
            rental.returned = True
            rental.save()
            rental_return.save()

            if rental_return.totalFee == 0:
                return HttpResponseRedirect('/homepage/rentals')
            else:
                return HttpResponseRedirect('/homepage/checkout.pay_rental_fees/{}/'.format(rental_return.id))


    params['form'] = form
    params['rented_items'] = rented_items
    params['rental'] = rental
    params['now'] = now
    return templater.render_to_response(request, 'rentals.rental_return.html', params)

class fee_form(forms.Form):
    damageFee = forms.DecimalField(
        label="Damage Fee ($):",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','id': 'box1'}))
    lateFee = forms.DecimalField(
        label="Late Fee ($):",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control','id':'box2'}))
    totalFee = forms.DecimalField(
        label="Total Fee ($):",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control','id':'total'}))

@view_function
def change_condition(request):
    params = {}
    rid = request.urlparams[0]
    new_condition = request.urlparams[1]

    try:
        rented_item = hmod.RentedItem.objects.get(id=rid)
        item = hmod.Item.objects.get(id=rented_item.item_id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    item.condition = new_condition
    item.save()

    return HttpResponseRedirect('/homepage/rentals/')

@view_function
def send_email(request):
    params={}
    
    now = datetime.now()
    thirty = timezone.now() - timedelta(days=30)
    sixty = timezone.now() - timedelta(days=60)
    ninety = timezone.now() - timedelta(days=90)

    # try:
    #     params['rentals'] = hmod.Rental.objects.all()
    # except hmod.Event.DoesNotExist:
    #     raise HttpResponseRedirect('/homepage/index/')

    try:
        late_rentals = hmod.Rental.objects.filter(dueDate__lte=now).order_by('dueDate')
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    # try:
    #     today_to_thirty = hmod.Rental.objects.filter(dueDate__lte=now,dueDate__gt=thirty).order_by('dueDate')
    # except hmod.User.DoesNotExist:
    #     return HttpResponseRedirect('/homepage/rentals/')

    # try:
    #     thirty_to_sixty = hmod.Rental.objects.filter(dueDate__lte=thirty,dueDate__gt=sixty).order_by('dueDate')
    # except hmod.User.DoesNotExist:
    #     return HttpResponseRedirect('/homepage/rentals/')

    # try:
    #     sixty_to_ninety = hmod.Rental.objects.filter(dueDate__lte=sixty,dueDate__gt=ninety).order_by('dueDate')
    # except hmod.User.DoesNotExist:
    #     return HttpResponseRedirect('/homepage/rentals/')

    # try:
    #     ninety_plus = hmod.Rental.objects.filter(dueDate__lte=ninety).order_by('dueDate')
    # except hmod.User.DoesNotExist:
    #     return HttpResponseRedirect('/homepage/rentals/')

    if late_rentals:

        print(">>>>>>>>>>>>>>",late_rentals)
        for rental in late_rentals:
            try:
                user = hmod.User.objects.get(id=rental.memberName.id)
            except hmod.User.DoesNotExist:
                pass
            
            subject = "Late Rental Notice"
            message = templater.render(request, 'email_late_rentals.html', params)
            from_email = "mycolonialfoundation@gmail.com"
            to_email = user.email
            send_mail(subject, message, from_email,[to_email],html_message=message,fail_silently=False)
        

    # if today_to_thirty:
    #     print('yeah')

    # if thirty_to_sixty:
    #     print('yeah')

    # if sixty_to_ninety:
    #     print('yeah')

    # if ninety_plus:
    #     print('yeah')

    return HttpResponseRedirect('/homepage/rentals/')













