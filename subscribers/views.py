from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subscriber
from .serializers import SubscriberSerializer


@api_view(['POST'])
def add_subscriber_to_service(request):
    if request.method == 'POST':
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            service = serializer.validated_data['service']
            existing_subscriber = Subscriber.objects.filter(email=email, service=service).first()
            if existing_subscriber:
                return Response({"message": "You have already subscribed to this service."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"message": "You've successfully subscribe to this Service!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Invalid request method."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)