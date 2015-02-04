from django.conf import settings
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):
	params={}
	# try:
	# 	allRoles = hmod.Role.objects.all()
	# except Exception:
	# 	return HttpResponseRedirect("/homepage/about")
	try:
		allRoles = hmod.Role.objects.all()
		params['allRoles'] = allRoles
	except hmod.Role.DoesNotExist:
		raise e
	
	return templater.render_to_response(request, 'index.html', params)