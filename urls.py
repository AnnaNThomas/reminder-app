from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('reg/',views.reg,name="reg"),
    path('login/',views.login,name="login"),
    path('log/',views.log,name="log"),
 
    path('msg/',views.msg,name="msg"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('notification/',views.notification,name="notification"),
]
