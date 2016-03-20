from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.flatpages import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^modules/', include('notebook.urls_module')),
    url(r'^examples/', include('notebook.urls_example')),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<url>.*/)$', views.flatpage),
]
