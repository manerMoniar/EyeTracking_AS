"""eyetracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from apps.tracker import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tracker/', include('apps.tracker.urls', namespace="tracker")),
    url(r'^images/', include('apps.images.urls', namespace="images")),
    url(r'^participants/', include('apps.participants.urls', namespace="participants")),
    url(r'^aoi/', include('apps.aoi.urls', namespace="aoi")),
    url(r'^aoi2/', include('apps.aoi2.urls', namespace="aoi2")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
