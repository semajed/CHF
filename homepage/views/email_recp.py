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

@view_function
def process_request(request):
    params = {}

    rental_return_id = request.urlparams[0]
    try:
        rental_return = hmod.Return.objects.get(id=rental_return_id)
    except hmod.User.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')

    params['rental_return'] = rental_return
    return templater.render_to_response(request, 'thankyou.html', params)

@view_function
def products(request):
    params={}

    productDict = request.session['shopping_cart']
    cart_product_list = []
    for k,v in productDict.items():
        cart_product = hmod.cart_product.objects.get(id=k)
        cart_product_list.append(cart_product)

    params['cart_product_list'] = cart_product_list

    del request.session['shopping_cart']

    return templater.render_to_response(request, 'thankyou.html', params)

@view_function
def rentals(request):
    params={}

    itemDictionary = request.session['rental_cart']
    cart_item_list = []
    for k,v in itemDictionary.items():
        cart_item = hmod.cart_item.objects.get(id=k)
        cart_item_list.append(cart_item)

    params['cart_item_list'] = cart_item_list

    # item_list = request.session['rental_cart']
    # item_list2 = []
    # for k,v in item_list.items():
    #     item = hmod.Item.objects.get(id=k)
    #     item_list2.append(item)

    # params['qty'] = request.urlparams[0]
    # params['item_list2'] = item_list2

    del request.session['rental_cart']

    return templater.render_to_response(request, 'thankyou.html', params)



















