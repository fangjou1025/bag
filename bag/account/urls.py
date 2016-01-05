from django.conf.urls import url
from account import views


urlpatterns = [
               url(r'^register/$', views.register, name='register'),
               url(r'^userLogin/$', views.userLogin, name='userLogin'),
               url(r'^userLogout/$', views.userLogout, name='userLogout'),
]
