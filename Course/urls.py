from django.urls import path
from.views import *

app_name='Course'

urlpatterns=[
    path('course',course,name='course'),
]