from django.shortcuts import render

from .services import get_nearby_hospitals
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home_page(request):
    return render(request,"hospitals/index.html")

def results_page(request):
    return render(request, "hospitals/results.html")

@api_view(['GET'])
def health_check(request):
    return Response({"status":"MediCare backend running"})

@api_view(['POST'])
def receive_location(request):
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')

    return Response({
        "received_latitude": latitude,
        "received_longitude": longitude
    })

@api_view(['POST'])
def nearby_hospitals(request):
    lat = request.data.get("latitude")
    lon = request.data.get("longitude")

    hospitals = get_nearby_hospitals(lat, lon)

    return Response({
        "your_location": {"lat": lat, "lon": lon},
        "hospitals": hospitals
    })
