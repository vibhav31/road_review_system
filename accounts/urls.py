
from django.urls import path
from .import views

urlpatterns = [
    path('registeruser/', views.register_user),
    path('login/',views.login),
    path('dashboard/',views.dashboard),
    path('logout/',views.logout),
    path('guest_register/',views.guest_register),


]
