from django.urls import path
from .views import add_subscriber_to_service

app_name = "subscribers"

urlpatterns = [
    path('api/add-subscriber/', add_subscriber_to_service, name='add-subscriber'),
]
