from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='custom_login'),
    path('createteam/',views.createteam,name='createteam'),
    path('success/', views.success, name='success'),  
]
