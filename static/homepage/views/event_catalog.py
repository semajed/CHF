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
        params['events'] = hmod.Event.objects.all()
    except hmod.Product.DoesNotExist:
        raise e

    return templater.render_to_response(request, 'event_catalog.html', params)



################### detail catalog PAGE ###########################

@view_function
def detail(request):
    params={}

    event_id = request.urlparams[0]

    try:
        event = hmod.Event.objects.get(id=event_id)
        venue = hmod.Venue.objects.get(id=event.venue.id)
        address = hmod.Address.objects.get(id=venue.location.id)
        areas = hmod.Area.objects.filter(event=event)
        saleitem_list = hmod.SaleItem.objects.filter(event=event)
    except hmod.Product.DoesNotExist:
        raise e

    params['event'] = event
    params['venue'] = venue
    params['address'] = address
    params['areas'] = areas
    params['saleitem_list'] = saleitem_list
    return templater.render_to_response(request, 'event_catalog.detail.html', params)
















