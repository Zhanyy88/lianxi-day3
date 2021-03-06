"""day3 URL Configuration

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

from app01 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #  ======  JsonResponse案例===============
    url(r'^get_json/$', views.get_json),
    url(r'^do_json/$', views.do_json),

    # =========Cookie案例====================
    url(r'^set_cookie/$',views.set_cookie),
    url(r'^get_cookie/$',views.get_cookie),

    # =========Session案例====================
    url(r'^set_session/$',views.set_session),
    url(r'^get_session/$',views.get_session),
]
