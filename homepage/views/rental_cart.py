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

templater = get_renderer('homepage')

################### view rental cart ###########################

@view_function
def process_request(request):
    params={}

    itemDictionary = request.session['rental_cart']
    cart_item_list = []
    for k,v in itemDictionary.items():
        # item = hmod.Item.objects.get(id=k)
        # itemList2.append(item)
        cart_item = hmod.cart_item.objects.get(id=k)
        cart_item_list.append(cart_item)

    params['cart_item_list'] = cart_item_list
    return templater.render_to_response(request, 'rental_cart.html', params)



################### add to rental cart ###########################

@view_function
def add(request):
    params={}

#ensure that the session has a rental cart
    if 'rental_cart' not in request.session:
        request.session['rental_cart'] = {}
    pid = request.urlparams[0]
    # qty = request.urlparams[1]
    # params['qty'] = qty
    
#add the item to the rental cart
    if pid in request.session['rental_cart']:
        request.session['rental_cart'][pid] += 1
        request.session.modified = True
    else:
        request.session['rental_cart'][pid] = 1
        request.session.modified = True


    itemDictionary = request.session['rental_cart']
    itemList2 = []
    cart_item_list = []
    for k,v in itemDictionary.items():
        item = hmod.Item.objects.get(id=k)
        # itemList2.append(item)
        cart_item = hmod.cart_item()
        cart_item.id = item.id
        cart_item.name = item.name
        cart_item.value = item.value
        cart_item.STP = item.STP
        cart_item.qty = v
        cart_item.condition = item.condition
        cart_item.photo = item.photo
        cart_item.save()
        cart_item_list.append(cart_item)

    params['cart_item_list'] = cart_item_list
    params['itemList2'] = itemList2
    return templater.render_to_response(request, 'rental_cart.html', params)

################### remove from rental cart ###########################

@view_function
def remove(request):
    params={}

    pid = request.urlparams[0]
    qty = request.urlparams[1]

    del request.session['rental_cart'][pid]
    request.session.modified = True

    sesh = request.session['rental_cart']
    itemList2 = []
    for k,v in sesh.items():
        item = hmod.Item.objects.get(id=k)
        itemList2.append(item)


    params['itemList2'] = itemList2
    params['qty'] = qty
    return templater.render_to_response(request, 'rental_cart.html', params)

################### check login before checking out ###########################

@view_function
def check_login(request):
    params={}

    if request.user.is_authenticated():
        return HttpResponseRedirect('/homepage/checkout.checkout_rental/')
    else:
        return HttpResponseRedirect('/homepage/base.loginform/')




















