"""test_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from form import views
from form.views import index

urlpatterns = [
    path('', index ),
    url(r'^index/$', views.index, name='index'),
    url(r'^t_linegraph/$', views.t_linegraph, name='t_linegraph'),
    url(r'^r_linegraph/$', views.r_linegraph, name='r_linegraph'),
    url(r'^t_piechart/$', views.piechart, name='piechart'),
    url(r'^t_bargraph/$', views.bargraph, name='bargraph'),
    url(r'^wordcloud/$', views.wordcloud, name='wordcloud'),
    url(r'^locationcloud/$', views.locationcloud, name='locationcloud'),
    path('admin/', admin.site.urls),
]
