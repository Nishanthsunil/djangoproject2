from . import views
from django.urls import path

urlpatterns=[
    path("",views.demo,name='demo'),
    path("login",views.login,name="login"),
    path("w",views.w,name='w'),
]