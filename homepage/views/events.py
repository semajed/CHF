from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime
from django.utils import formats
from django.contrib.auth.decorators import permission_required, user_passes_test
import homepage.models as hmod


templater = get_renderer('homepage')

################### USER PAGE ###########################
@view_function
# @permission_required('events.add_event', login_url='/homepage/login/')
@user_passes_test(lambda u: u.groups.filter(name="Manager") or u.is_superuser,login_url='/homepage/login/')
def process_request(request):
	params={}

	try:
		params['events'] = hmod.Event.objects.all()
	except hmod.Event.DoesNotExist:
		raise HttpResponseRedirect('/homepage/index/')

	return templater.render_to_response(request, 'events.html', params)


################### EDIT USER ###########################
@view_function
def edit(request):
	params={}

	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except hmod.Event.DoesNotExist:
		raise HttpResponseRedirect('/homepage/events/')
	
	form = EventEditForm(initial={
		'name': event.name,
		'startDate': event.startDate.strftime('%m/%d/%Y'),
		'endDate': event.endDate.strftime('%m/%d/%Y'),
		})
	if request.method == 'POST':
		form = EventEditForm(request.POST)
		if form.is_valid():
			event.name = form.cleaned_data['name']
			event.startDate = datetime.strptime(form.cleaned_data['startDate'], '%m/%d/%Y')
			event.endDate = datetime.strptime(form.cleaned_data['endDate'], '%m/%d/%Y')
			event.save()
			return HttpResponseRedirect('/homepage/events')


	params['form'] = form
	params['event'] = event
	return templater.render_to_response(request, 'events.edit.html', params)


class EventEditForm(forms.Form):
	name = forms.CharField(
		required=True,
		min_length=1,
		max_length=100,
		widget=forms.TextInput(attrs=
			{
			'class': 'form-control'
			}))
	startDate = forms.CharField(
		required=True,
		widget=forms.TextInput(attrs=
            {
                'class':'datepicker'
            }))
	endDate = forms.CharField(
		required=True,
		widget=forms.TextInput(attrs=
            {
                'class':'datepicker'
            }))

	def clean_name(self):
		if len(self.cleaned_data['name']) < 5:
			raise forms.ValidationError("Name of event must be longer than 5 characters")
		return self.cleaned_data['name']

	def clean_endDate(self):
		if self.cleaned_data['endDate'] < self.cleaned_data['startDate']:
			raise forms.ValidationError("The end date must be after the start date")
		return self.cleaned_data['endDate']

#this check is to prevent a user from choosing a day in the past.
#will this functionality be needed though?
	# def clean_startDate(self):
	# 	now = datetime.now().strftime('%m/%d/%Y')
	# 	if self.cleaned_data['startDate'] < now:
	# 		raise forms.ValidationError("The start date must be in the future")
	# 	return self.cleaned_data['startDate']


################### CREATE EVENT ###########################
@view_function
def create(request):
	params={}

	event1 = hmod.Event()

	event1.name = ""
	event1.startDate = datetime.now()
	event1.endDate = datetime.now()
	event1.save()


	return HttpResponseRedirect('/homepage/events.edit/{}/'.format(event1.id))


################### DELETE USER ###########################
@view_function
def delete(request):
	params={}
	
	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except hmod.Event.DoesNotExist:
		return HttpResponseRedirect('/homepage/events/')

	event.delete()

	return HttpResponseRedirect('/homepage/events/')












