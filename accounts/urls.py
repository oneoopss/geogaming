from django.urls import path
from accounts import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('signup', views.signupuser, name='signupuser'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),
    path('events', views.events, name='events'),
    path('cat', views.cat, name='cat'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
