from django.contrib import admin
from django.urls import include, path
from hospitals.views import home_page, results_page


urlpatterns = [
    path('',home_page),
    path('result/',results_page),
    path('admin/', admin.site.urls),
    path('api/',include('hospitals.urls')),
]
