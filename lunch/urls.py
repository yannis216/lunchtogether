from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lunchrequest_new, name='lunchrequest_new'),
    url(r'^lunch/(?P<pk>\d+)/$', views.lunch_confirm, name='lunch_confirm'),
]
