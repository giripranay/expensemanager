from django.conf.urls import url
from . import views


urlpatterns=[
       url(r'^$',views.index,name='index'), 
       url(r'^addnew$',views.addnew,name='addnew'),
       url(r'^graph$',views.graph,name='graph'),
       url(r'^food$',views.food,name='food'),
       url(r'^grocery$',views.grocery,name='grocery'),
       url(r'^petrol$',views.petrol,name='petrol'),
       url(r'^entertainment$',views.entertainment,name='entertainment'),
    ]
