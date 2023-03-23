from . import views
from django.urls import path

urlpatterns = [
    path('',views.register,name='reg'),
    path('login',views.login,name='login'),
    path('re',views.re,name='re')
    ]