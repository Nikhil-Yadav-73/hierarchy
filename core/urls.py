
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("signin/", views.signin, name='signin'),
    path("register/", views.register, name='register'),
    path('logout/', views.logout_user, name='logout')
]
