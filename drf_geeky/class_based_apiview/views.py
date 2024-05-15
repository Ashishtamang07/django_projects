from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from rest_framework.views import APIView

class StudentAPI(APIView):
    def get(self, request, format=None, pk= None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu= Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data)
    # post data req -> recive into data=request.data and serialize it 
    def post(self, request, format=None):
        serializer= StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created '}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #update 
    def put(self, request, format=None, pk= None):
        id = pk
        stu= Student.objects.get(pk = id)
        serializer= StudentSerializer(stu, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated '})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #particail update
    def patch(self, request, format=None, pk= None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer= StudentSerializer(stu, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' partial Data updated '})
        return Response(serializer.errors)
    def delete(self, request, format=None, pk= None):
        id =pk
        stu= Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg':'Data deleted '})
    
        
        
