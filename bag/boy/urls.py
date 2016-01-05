from django.conf.urls import url
from boy import views


urlpatterns = [
    url(r'^$', views.boy, name='boy'),
 ]
