from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','core.views.upload_file',name='upload_file'),
    url(r'^(?P<slug>[\w\-]+)/$', 'core.views.data'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
           ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
