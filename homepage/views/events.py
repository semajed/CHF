from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function    
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import datetime
from django.utils import formats
import homepage.models as hmod


templater = get_renderer('homepage')

################### USER PAGE ###########################
@view_function
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

	# def clean_empname(self):
	# 	if len(self.cleaned_data['first_name']) < 5:
	# 		raise forms.ValidationError("Hey man, fix it")
	# 	try:
	# 		emp = hmod.User.objects.get(firstName=self.cleaned_data['firstName'])
	# 		raise forms.ValidationError("This user name is already taken bro")
	# 	except hmod.Employee.DoesNotExist:
	# 		pass # we want this!

# birthday = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y')), input_formats=('%m/%d/%Y',))

################### CREATE USER ###########################
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












