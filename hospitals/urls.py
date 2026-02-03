from django import views
from django.urls import path
from .views import health_check, nearby_hospitals, receive_location, results_page


urlpatterns = [
    path('health/', health_check),
    path('result/',results_page),
    path('location/', receive_location),
    path('hospitals/',nearby_hospitals),
    path('nearby/', nearby_hospitals),
]
