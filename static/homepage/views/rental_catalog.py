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
        params['items'] = hmod.Item.objects.all()
    except hmod.Item.DoesNotExist:
        raise e

    return templater.render_to_response(request, 'rental_catalog.html', params)



################### detail catalog PAGE ###########################

@view_function
def detail(request):
    params={}

    try:
        item = hmod.Item.objects.get(id=request.urlparams[0])
    except hmod.Item.DoesNotExist:
        raise e
    params['qty'] = request.urlparams[1]
    params['item'] = item
    return templater.render_to_response(request, 'rental_catalog.detail.html', params)
















