from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime, timedelta
from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required,user_passes_test
import homepage.models as hmod
from django.core.files import File
from .. import dmp_render, dmp_render_to_response
from django.core.mail import send_mail
from decimal import Decimal
import requests

templater = get_renderer('homepage')

MASTER_CARD = 'MC'
DISCOVER = 'D'
VISA = 'V'
type_choices = (
    (MASTER_CARD, "Master Card"),
    (DISCOVER, "Discover"),
    (VISA, "Visa"),
    )
JANUARY = '01'
FEBRUARY = '02'
MARCH = '03'
APRIL = '04'
MAY = '05'
JUNE = '06'
JULY = '07'
AUGUST = '08'
SEPTEMBER = '09'
OCTOBER = '10'
NOVEMBER = '11'
DECEMBER = '12'
month_choices = (
    (JANUARY, "01"),
    (FEBRUARY, "02"),
    (MARCH, "03"),
    (APRIL, "04"),
    (MAY, "05"),
    (JUNE, "06"),
    (JULY, "07"),
    (AUGUST, "08"),
    (SEPTEMBER, "09"),
    (OCTOBER, "10"),
    (NOVEMBER, "11"),
    (DECEMBER, "12"),
    )
y2015 = '15'
y2016 = '16'
y2017 = '17'
y2018 = '18'
year_choices = (
    (y2015, "2015"),
    (y2016, "2016"),
    (y2017, "2017"),
    (y2018, "2018"),
    )

@view_function
def pay_rental_fees(request):
    params = {}
    return_id = request.urlparams[0]
    try:
        rental_return = hmod.Return.objects.get(id=return_id)
        user = hmod.User.objects.get(id=request.user.id)
        address = hmod.Address.objects.get(id=user.address.id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/rentals/')

    form1 = fee_form(initial={
        'damageFee': rental_return.damageFee,
        'lateFee': rental_return.lateFee,
        'totalFee': rental_return.totalFee,
        'street1': address.street1,
        'street2': address.street2,
        'city': address.city,
        'state': address.state,
        'ZIP': address.ZIP,
        'holder': user.get_full_name(),
        })
    if request.method == 'POST':
        form = fee_form(request.POST)
        if form.is_valid():
            rental_return.damageFee = form.cleaned_data['damageFee']
            rental_return.lateFee = form.cleaned_data['lateFee']
            rental_return.totalFee = form.cleaned_data['totalFee']
            rental_return.returnTime = datetime.now()
            rental_return.user = request.user
            address.street1 = form.cleaned_data['street1']
            address.street2 = form.cleaned_data['street2']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.ZIP = form.cleaned_data['ZIP']
            rental_return.save()

            subject = "Rental Payment - Thank You"
            params['rental_return'] = rental_return
            message = templater.render(request, 'email_recp.html', params)
            from_email = "mycolonialfoundation@gmail.com"
            to_email = request.user.email
            send_mail(subject, message, from_email,[to_email],html_message=message,fail_silently=False)

            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '94b459fe32adabeddfc3e6d0fe9265d1'
            # description = request.user.get_full_name() + " is purchasing product(s)"
            # typeof = str(form.cleaned_data['card_type'])
            # expm = "0" + str(form.cleaned_data['exp_month'])
            # expy = int(form.cleaned_data['exp_year'])
            # cv = str(form.cleaned_data['CVC'])

            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency':'usd',
                'amount':'5.99', 
                'type':'Visa',
                'number':'4732817300654',
                'exp_month':10, 
                'exp_year':15,
                'cvc':411,
                'name':'Cosmo Limesandal', 
                'description':'Charge for cosmo@is411.byu.edu',
                })
            #debug with printing the response
            print(r.text)

            #parse the response to a dictionary
            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])
            else:
                print(">>>>>>>>",resp.keys())
                print(">>>>>>>>",resp['ID'])

            return HttpResponseRedirect('/homepage/thankyou/{}'.format(rental_return.id))

    params['form1'] = form1
    params['rental_return'] = rental_return
    return templater.render_to_response(request, 'checkout.html', params)

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
    holder = forms.CharField(
        label="Credit Card Holder:",
        required=True,
        min_length=1,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    creditCard = forms.CharField(
        label="Credit Card Number:",
        required=True,
        min_length=16,
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'xxxx-xxxx-xxxx-xxxx'}))
    CVC = forms.CharField(
        label="CVC:",
        required=True,
        min_length=3,
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'xxx'}))
    exp_month = forms.ChoiceField(
        label="Expiration Month:",
        required=True,
        choices=month_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))
    exp_year = forms.ChoiceField(
        label="Expiration Year:",
        required=True,
        choices=year_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))
    card_type = forms.ChoiceField(
        label="Card Type:",
        required=True,
        choices=type_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))



@view_function
def checkout_product(request):
    params = {}
######### prepare the shopping cart to be reviewed###################
    product_list = request.session['shopping_cart']
    product_list2 = []
    for k,v in product_list.items():
        product = hmod.Product.objects.get(id=k)
        product_list2.append(product)

    params['product_list2'] = product_list2
    params['qty'] = request.urlparams[0]

###############handle the form############

    try:
        user = hmod.User.objects.get(id=request.user.id)
        address = hmod.Address.objects.get(id=user.address.id)
    except hmod.User.DoesNotExist:
        raise HttpResponseRedirect('/homepage/catalog/')

    shipping = hmod.Address()
    shipping = address
    shipping.save()

    order = hmod.Order()
    order.orderDate = datetime.now()
    order.trackingNumber = 1
    order.shippingAddress = shipping
    order.totalCost = 0.00
    totalCost = Decimal(order.totalCost)
    for p in product_list2:
        price = Decimal(p.currentPrice)
        totalCost = totalCost + p.currentPrice
    order.totalCost = totalCost
    params['order'] = order

    form = product_checkoutForm(initial={
        'street1': shipping.street1,
        'street2': shipping.street2,
        'city': shipping.city,
        'state': shipping.state,
        'ZIP': shipping.ZIP,
        'holder': user.get_full_name(),
        })
    if request.method == 'POST':
        form = product_checkoutForm(request.POST)
        if form.is_valid():
            shipping.street1 = form.cleaned_data['street1']
            shipping.street2 = form.cleaned_data['street2']
            shipping.city = form.cleaned_data['city']
            shipping.state = form.cleaned_data['state']
            shipping.ZIP = form.cleaned_data['ZIP']
            order.nameOnCard = form.cleaned_data['holder']
            order.creditCard = form.cleaned_data['creditCard']
            shipping.save()
            order.save()

            subject = "Product Purchase - Thank You"
            params['user'] = user

            message = templater.render(request, 'email_recp.html', params)
            from_email = "mycolonialfoundation@gmail.com"
            to_email = request.user.email
            send_mail(subject, message, from_email,[to_email],html_message=message,fail_silently=False)

            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '94b459fe32adabeddfc3e6d0fe9265d1'
            # description = request.user.get_full_name() + " is purchasing product(s)"
            # typeof = str(form.cleaned_data['card_type'])
            # expm = "0" + str(form.cleaned_data['exp_month'])
            # expy = int(form.cleaned_data['exp_year'])
            # cv = str(form.cleaned_data['CVC'])

            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency':'usd',
                'amount':'5.99', 
                'type':'Visa',
                'number':'4732817300654',
                'exp_month':10, 
                'exp_year':15,
                'cvc':411,
                'name':'Cosmo Limesandal', 
                'description':'Charge for cosmo@is411.byu.edu',
                })
            #debug with printing the response
            print(r.text)

            #parse the response to a dictionary
            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])
            else:
                print(">>>>>>>>",resp.keys())
                print(">>>>>>>>",resp['ID'])





            return HttpResponseRedirect('/homepage/thankyou.products/')


    params['form'] = form
    params['user'] = user
    return templater.render_to_response(request, 'checkout.html', params)

class product_checkoutForm(forms.Form):
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
    holder = forms.CharField(
        label="Credit Card Holder:",
        required=True,
        min_length=1,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    creditCard = forms.CharField(
        label="Credit Card Number:",
        required=True,
        min_length=16,
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'xxxx-xxxx-xxxx-xxxx'}))
    CVC = forms.CharField(
        label="CVC:",
        required=True,
        min_length=3,
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'xxx'}))
    exp_month = forms.ChoiceField(
        label="Expiration Month:",
        required=True,
        choices=month_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))
    exp_year = forms.ChoiceField(
        label="Expiration Year:",
        required=True,
        choices=year_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))
    card_type = forms.ChoiceField(
        label="Card Type:",
        required=True,
        choices=type_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))




################### checkout for rentals ###########################
@view_function
def checkout_rental(request):
    params={}

    item_list = request.session['rental_cart']
    item_list2 = []
    for k,v in item_list.items():
        item = hmod.Item.objects.get(id=k)
        item_list2.append(item)

        params['item_list2'] = item_list2
        params['qty'] = request.urlparams[0]

    ###############handle the form############

    try:
        user = hmod.User.objects.get(id=request.user.id)
        address = hmod.Address.objects.get(id=user.address.id)
    except hmod.User.DoesNotExist:
        raise HttpResponseRedirect('/homepage/catalog/')

    rental = hmod.Rental()
    rental.rentalTime = datetime.now()
    rental.dueDate = rental.rentalTime + timedelta(days=7)
    rental.totalCost = 0.00
    r_totalCost = Decimal(rental.totalCost)
    for i in item_list2:
        r_totalCost = r_totalCost + item.STP
    rental.totalCost = r_totalCost
    params['rental'] = rental

    form = rental_checkoutForm(initial={
        'rentee': user.get_full_name(),
        'dueDate': rental.dueDate.strftime('%m/%d/%Y'),
        'discountPercent': 0,
        'street1': address.street1,
        'street2': address.street2,
        'city': address.city,
        'state': address.state,
        'ZIP': address.ZIP,
        'holder': user.get_full_name(),
        })
    if request.method == 'POST':
        form = rental_checkoutForm(request.POST)
        if form.is_valid():
            rental.memberName = user
            rental.dueDate = datetime.strptime(form.cleaned_data['dueDate'],'%m/%d/%Y')
            rental.handlingAgent = user
            rental.discountPercent = form.cleaned_data['discountPercent']
            address.street1 = form.cleaned_data['street1']
            address.street2 = form.cleaned_data['street2']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.ZIP = form.cleaned_data['ZIP']
            rental.nameOnCard = form.cleaned_data['holder']
            rental.creditCard = form.cleaned_data['creditCard']
            rental.save()

            subject = "Rental Payment - Thank You"
            # params['user'] = user
            message = templater.render(request, 'email_recp.html', params)
            from_email = "mycolonialfoundation@gmail.com"
            # to_email = ['brandonpwanlass@gmail.com','vjsoffe@gmail.com','nicholas.allegretti@gmail.com','dayhuffj@gmail.com']
            # for email in to_email:
            #     send_mail(subject, message, from_email,[email],html_message=message,fail_silently=False)
            to_email = request.user.email

            send_mail(subject, message, from_email,[to_email],html_message=message,fail_silently=False)

            API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
            API_KEY = '94b459fe32adabeddfc3e6d0fe9265d1'
            # description = request.user.get_full_name() + " is purchasing product(s)"
            # typeof = str(form.cleaned_data['card_type'])
            # expm = "0" + str(form.cleaned_data['exp_month'])
            # expy = int(form.cleaned_data['exp_year'])
            # cv = str(form.cleaned_data['CVC'])

            r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency':'usd',
                'amount':'5.99', 
                'type':'Visa',
                'number':'4732817300654',
                'exp_month':10, 
                'exp_year':15,
                'cvc':411,
                'name':'Cosmo Limesandal', 
                'description':'Charge for cosmo@is411.byu.edu',
                })
            #debug with printing the response
            print(r.text)

            #parse the response to a dictionary
            resp = r.json()
            if 'error' in resp:
                print("ERROR: ", resp['error'])
            else:
                print(">>>>>>>>",resp.keys())
                print(">>>>>>>>",resp['ID'])

            for i in item_list2:
                ri = hmod.RentedItem()
                ri.rental = rental
                ri.item = i
                ri.save()

            qty = request.urlparams[0]
            return HttpResponseRedirect('/homepage/thankyou.rentals/{}'.format(qty))


    params['form'] = form
    params['user'] = user

    ############### prepare the forms to be filled out ##################

    return templater.render_to_response(request, 'checkout.html', params)


class rental_checkoutForm(forms.Form):
    rentee = forms.CharField(
        label="Rentee:",
        required=True,
        min_length=1,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    dueDate = forms.CharField(
        label="Due Date:",
        required=True,
        widget=forms.TextInput(attrs={'class':'datepicker form-control','id':'due_date'}))
    # handlingAgent = forms.ModelChoiceField(
    #     label="Handling Agent:",
    #     queryset=hmod.User.objects.filter(is_agent=True),
    #     required=True,
    #     widget=forms.Select(attrs={'class': 'form-control'}))
    discountPercent = forms.CharField(
        label="Discount Percent:",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # condition = forms.ChoiceField(
    #     label="Condition:",
    #     required=True,
    #     choices=CONDITION_CHOICES,
    #     widget=forms.Select(attrs={'class': 'form-control'}))
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
    holder = forms.CharField(
        label="Credit Card Holder:",
        required=True,
        min_length=1,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    creditCard = forms.CharField(
        label="Credit Card Number:",
        required=True,
        min_length=16,
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'xxxx-xxxx-xxxx-xxxx'}))
    CVC = forms.CharField(
        label="CVC:",
        required=True,
        min_length=3,
        max_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'xxx'}))
    exp_month = forms.ChoiceField(
        label="Expiration Month:",
        required=True,
        choices=month_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))
    exp_year = forms.ChoiceField(
        label="Expiration Year:",
        required=True,
        choices=year_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))
    card_type = forms.ChoiceField(
        label="Card Type:",
        required=True,
        choices=type_choices,
        widget=forms.Select(attrs={'class': 'form-control'}))


























