from django.conf.urls import url
from django.urls import path
from App_Login import views
# app_name='account'

urlpatterns = [
    path('SignUp/', views.SignUp, name='Signup'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.logout, name='Logout'),
    path('home/', views.index, name='home'),
    path('', views.index, name='home'),

]
