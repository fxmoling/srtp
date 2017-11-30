from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^upload/uploading$', views.do_upload, name='do_upload'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.my_login, name='login'),
    url(r'^sample$', views.sample, name='sample'),
]






