from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def get_data(request):
    student_obj= Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)
    person= {"name": "ashish", "age":25}
    return Response({"status": 200, "payload": serializer.data})


@api_view(['POST'])
def post_student(request):
    # data = request.data
    serializer= StudentSerializer(data= request.data)
    
    if not serializer.is_valid():
        return Response({"status": 403, "payload": serializer.errors, "message":"something went wrong"})
    serializer.save()
    # print(data)
  
    return Response({"status": 200, "payload": serializer.data, "message":"you sent data"})

@api_view(['PUT'])
def update_student(request , id):
    try:
        student_obj= Student.objects.get(id=id)
        
        serializer= StudentSerializer(student_obj, data= request.data, partial =True)

        if not serializer.is_valid():
            return Response({"status": 403, "payload": serializer.errors, "message":"something went wrong"})
        serializer.save()
        # print(data)
    
        return Response({"status": 200, "payload": serializer.data, "message":"you sent data"})
    except  Exception as e:
        return Response({"status": 403,"message":"invalide id"})


