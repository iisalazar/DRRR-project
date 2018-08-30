from django.urls import path
from . import views
app_name = 'weather_forecast'
urlpatterns = [
    path('', views.home, name='weather-forecast')
]