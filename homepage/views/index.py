from django.conf import settings
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import homepage.models as hmod
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params={}

	
	return templater.render_to_response(request, 'index.html', params)