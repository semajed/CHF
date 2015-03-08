from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_dmp1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'test_dmp1.templates.contact',name='contact'),

    url(r'^admin/', include(admin.site.urls)),
    # the django_mako_plus controller handles every request - this line is the glue that connects Mako to Django
	url(r'^.*$', 'django_mako_plus.controller.router.route_request' ),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})

)
 # + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
