from django.urls import path
from .views import *
app_name='Bootcamp'


urlpatterns=[
    path('bootcamp',bootcamp,name='bootcamp')
]