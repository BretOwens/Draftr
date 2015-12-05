"""mysite URL Configuration

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
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^qb/$', 'nfl.views.qb', name='qb'),
    url(r'^$', 'nfl.views.index', name='index'),
    url(r'^home/$', 'nfl.views.index', name='index'),
    url(r'^rb/$', 'nfl.views.rb', name='rb'),    
    url(r'^fb/$', 'nfl.views.fb', name='fb'),
    url(r'^wr/$', 'nfl.views.wr', name='wr'),
    url(r'^te/$', 'nfl.views.te', name='te'),
    url(r'^kicker/$', 'nfl.views.kicker', name='kicker'),
    url(r'^defense/$', 'nfl.views.defense', name='defense'),

]
