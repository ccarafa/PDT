"""trydjango URL Configuration

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
	url(r'^$', 'pdt.views.home', name='home'),
	url(r'^minception/$', 'pdt.views.minception', name='minception'),
	url(r'^minceptionopen/$', 'pdt.views.minceptionopen', name='minceptionopen'),
	url(r'^minceptionclose/$', 'pdt.views.minceptionclose', name='minceptionclose'),
	url(r'^minceptioniterations/$', 'pdt.views.minceptioniterations', name='minceptioniterations'),
	url(r'^melaborationiterations/$', 'pdt.views.melaborationiterations', name='melaborationiterations'),
	url(r'^mtransitioniterations/$', 'pdt.views.mtransitioniterations', name='mtransitioniterations'),
	url(r'^mconstructioniterations/$', 'pdt.views.mconstructioniterations', name='mconstructioniterations'),
	url(r'^melaboration/$', 'pdt.views.melaboration', name='melaboration'),
	url(r'^mconstruction/$', 'pdt.views.mconstruction', name='mconstruction'),
	url(r'^mtransition/$', 'pdt.views.mtransition', name='mtransition'),
	url(r'^developer/$', 'pdt.views.developer', name='developer'),
	url(r'^miteration/$', 'pdt.views.miteration', name='miteration'),
    url(r'^admin/', include(admin.site.urls)),
]
