from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('specific2/',specific2,name='specific2'),
]