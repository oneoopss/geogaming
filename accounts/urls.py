from django.urls import path
from accounts import views

urlpatterns = [
    path('signup', views.signupuser, name='signupuser'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),
    path('events', views.events, name='events'),
]
