from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.contrib.auth.decorators import permission_required,user_passes_test
import homepage.models as hmod

templater = get_renderer('homepage')

################### catalog PAGE ###########################
@view_function
# @permission_required('product.add_product', login_url='/homepage/login/')
#@user_passes_test(lambda u: u.groups.filter(name="Manager") or u.is_superuser,login_url='/homepage/login/')
def process_request(request):
    params={}

    try:
        params['products'] = hmod.Product.objects.all()
    except hmod.Product.DoesNotExist:
        raise e

    return templater.render_to_response(request, 'catalog.html', params)



################### detail catalog PAGE ###########################

@view_function
def detail(request):
    params={}

    try:
        product = hmod.Product.objects.get(id=request.urlparams[0])
    except hmod.Product.DoesNotExist:
        raise e
    params['qty'] = request.urlparams[1]
    params['product'] = product
    return templater.render_to_response(request, 'catalog.detail.html', params)
















