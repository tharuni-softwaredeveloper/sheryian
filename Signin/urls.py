from django.urls import path
from .views import *

app_name='Signin'

urlpatterns=[
    path('signin',signin,name='signin'),
]