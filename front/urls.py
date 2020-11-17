
from django.urls import path
from . import views

urlpatterns = [
    path('roadpage/', views.roadpage),
    path('',views.home),
    path('roaddetails/<id>',views.roaddetails),
    path('roadcategory/<id>', views.roadcategory),


]
