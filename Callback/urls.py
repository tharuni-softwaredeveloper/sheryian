from django.urls import path
from .views import *
app_name='Callback'


urlpatterns=[
    path('callback',callback,name='callback')
]