"""pdt URL Configuration

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
    url(r'^$', 'login.views.login', name='login_pattern'),
    url(r'^loggedin/$', 'login.views.loggedin'),
    url(r'^manager/$', 'login.views.manager'),
    url(r'^managerprojects/$', 'login.views.managerprojects'),
    url(r'^projectpage/$', 'login.views.projectpage'),
    url(r'^add_developer/$', 'login.views.add_developer'),
    url(r'^add_message/$', 'login.views.add_message'),
    url(r'^projectpage/projectbuttons/$', 'login.views.projectbuttons'),
    url(r'^developer/$', 'login.views.developer'),
    url(r'^auth/$', 'login.views.auth_view'),
    url(r'^curruser/$','login.views.curruser', name='curruser_pattern'),
    url(r'^projectpage/projectbuttons/projectdata/$', 'login.views.projectdata'),
    url(r'^projectpage/projectbuttons/phase/$', 'login.views.phase'),
    url(r'^developerphases/$', 'login.views.developerphases'),
    url(r'^developerinceptioniterations/$', 'login.views.developerinceptioniterations'),
    url(r'^developerelaborationiterations/$', 'login.views.developerelaborationiterations'),
    url(r'^developerconstructioniterations/$', 'login.views.developerconstructioniterations'),
    url(r'^developertransitioniterations/$', 'login.views.developertransitioniterations'),
    url(r'^calculatemetrics/$', 'login.views.phaseviewmetrics', name='phaseviewmetrics'),
	url(r'^calculatemetrics/$', 'login.views.projectviewmetrics', name='projectviewmetrics'),
	url(r'^calculatemetrics/$', 'login.views.iterationviewmetrics', name='iterationviewmetrics'),
    url(r'^projectpage/projectbuttons/phase/iteration/$', 'login.views.iteration', name='iteration'),
    url(r'^activities/$', 'login.views.activityDashboard', name="activityDashboard"),
    url(r'^activities/development/$', 'login.views.developmentActivity', name="developmentActivity"),
    url(r'^activities/defect_removal/$', 'login.views.defectsActivity', name="defectsActivity"),
    url(r'^activities/management/$', 'login.views.managementActivity', name="managementActivity"),
]
