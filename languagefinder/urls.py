from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('hello', views.hello, name='hello'),
    path('api/markers', views.sendJsonMarkers, name='sendJsonMarkers'),
    path('language/new', views.newLanguage, name='newLanguage')
]