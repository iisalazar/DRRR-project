from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.ContentList.as_view(), name="content_list")
]