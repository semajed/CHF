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
def products(request):
    params={}

    product_list = request.session['shopping_cart']
    product_list2 = []
    for k,v in product_list.items():
        product = hmod.Product.objects.get(id=k)
        product_list2.append(product)

    params['qty'] = request.urlparams[0]
    params['product_list2'] = product_list2

    del request.session['shopping_cart']

    return templater.render_to_response(request, 'thankyou.html', params)

@view_function
def rentals(request):
    params={}

    item_list = request.session['rental_cart']
    item_list2 = []
    for k,v in item_list.items():
        item = hmod.Item.objects.get(id=k)
        item_list2.append(item)

    params['qty'] = request.urlparams[0]
    params['item_list2'] = item_list2

    del request.session['rental_cart']

    return templater.render_to_response(request, 'thankyou.html', params)



















