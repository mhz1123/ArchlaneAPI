from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import User_dataSerializer, User_createSerializer
from .models import User_data
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser

@api_view(['GET'])
def getUsr(request):
    userData = User_data.objects.all()
    serializer = User_dataSerializer(userData, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def postUsr(request):
    data  = request.data
    user = User_data.objects.create(
        username = data['username'],
        password = data['password']
    )
    # serializer = User_dataSerializer(user, many = True)
    # return Response(serializer.data)
    return Response("Successfull")