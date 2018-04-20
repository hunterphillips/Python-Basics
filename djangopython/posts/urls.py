from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')
    # url('details/<int:id>', views.details, name='details') # django 2.0 syntax
] 
