from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('first_2/',first_2,name='first_2'),
    path('second_2/',second_2,name='second_2'),
]