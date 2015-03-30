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

templater = get_renderer('homepage')

################### get chopping cart ###########################

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
    order.save()

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

            qty = request.urlparams[0]


            return HttpResponseRedirect('/homepage/thankyou.products/{}'.format(qty))


    params['form'] = form
    params['user'] = user

    ############### prepare the forms to be filled out ##################




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
        min_length=1,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))



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
            rental.handlingAgent = form.cleaned_data['handlingAgent']
            rental.discountPercent = form.cleaned_data['discountPercent']
            address.street1 = form.cleaned_data['street1']
            address.street2 = form.cleaned_data['street2']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.ZIP = form.cleaned_data['ZIP']
            rental.nameOnCard = form.cleaned_data['holder']
            rental.creditCard = form.cleaned_data['creditCard']
            rental.save()
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
LOOKS_NEW = 'LN'
SLIGHTLY_USED = 'SU'
MODERATELY_USED = 'MU'
HEAVILY_USED = 'HU'
DESTROYED = 'D'
CONDITION_CHOICES = (
    (LOOKS_NEW, "Looks New"),
    (SLIGHTLY_USED, "Slightly Used"),
    (MODERATELY_USED, "Moderately Used"),
    (HEAVILY_USED, "Heavily Used"),
    (DESTROYED, "Destroyed"),
    )

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
        widget=forms.TextInput(attrs={'class':'datepicker'}))
    handlingAgent = forms.ModelChoiceField(
        label="Handling Agent:",
        queryset=hmod.User.objects.filter(is_agent=True),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}))
    discountPercent = forms.CharField(
        label="Discount Percent:",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    condition = forms.ChoiceField(
        label="Condition:",
        required=True,
        choices=CONDITION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
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
        min_length=1,
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))


























