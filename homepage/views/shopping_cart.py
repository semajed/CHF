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

################### add to shopping cart ###########################

@view_function
def process_request(request):
    params={}

    productDict = request.session['shopping_cart']
    cart_product_list = []
    for k,v in productDict.items():
        cart_product = hmod.cart_product.objects.get(id=k)
        cart_product_list.append(cart_product)

    params['cart_product_list'] = cart_product_list
    return templater.render_to_response(request, 'shopping_cart.html', params)



################### add to shopping cart ###########################

@view_function
def add(request):
    params={}

#ensure that the session has a shopping cart
    if 'shopping_cart' not in request.session:
        request.session['shopping_cart'] = {}
    pid = request.urlparams[0]
    # qty = request.urlparams[1]
    
    
#add the product to the shopping cart
    if pid in request.session['shopping_cart']:
        request.session['shopping_cart'][pid] += 1
        request.session.modified = True
        qty = request.session['shopping_cart'][pid]
    else:
        request.session['shopping_cart'][pid] = 1
        request.session.modified = True
        qty = request.session['shopping_cart'][pid]

    productDict = request.session['shopping_cart']
    productList2 = []
    cart_product_list = []
    for k,v in productDict.items():
        product = hmod.Product.objects.get(id=k)
        cart_product = hmod.cart_product()
        cart_product.id = product.id
        cart_product.name = product.name
        cart_product.currentPrice = product.currentPrice
        cart_product.photo = product.photo
        cart_product.qty = v
        cart_product.save()
        cart_product_list.append(cart_product)


    params['productList2'] = productList2
    params['cart_product_list'] = cart_product_list
    return templater.render_to_response(request, 'shopping_cart.html', params)

################### remove from shopping cart ###########################

@view_function
def remove(request):
    params={}

    pid = request.urlparams[0]
    qty = request.urlparams[1]

    del request.session['shopping_cart'][pid]
    request.session.modified = True

    productDict = request.session['shopping_cart']
    cart_product_list = []
    for k,v in productDict.items():
        cart_product = hmod.cart_product.objects.get(id=k)
        cart_product_list.append(cart_product)


    params['cart_product_list'] = cart_product_list
    return templater.render_to_response(request, 'shopping_cart.html', params)

################### remove from shopping cart ###########################

@view_function
def check_login(request):
    params={}

    params['qty'] = request.urlparams[0]

    if request.user.is_authenticated():
        return HttpResponseRedirect('/homepage/checkout.checkout_product/')
    else:
        return HttpResponseRedirect('/homepage/base.loginform/')



















