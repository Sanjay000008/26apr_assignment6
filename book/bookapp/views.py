from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
        AB=books.objects.all()
        serial=abooks(AB,many=True)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GEt'])
def getid(request,id):
    try:
        ABid=books.objects.get(id=id)
    except books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=abooks(ABid)
    return Response(data=serial.data,status=status.HTTP_200_OK)

@api_view(['GET','DELETE'])
def deletedata(request,id):
    try:
        ABid=books.objects.get(id=id)
    except books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        books.delete(ABid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=abooks(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        ABid=books.objects.get(id=id)
    except books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=abooks(ABid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=abooks(data=request.data,instance=ABid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)