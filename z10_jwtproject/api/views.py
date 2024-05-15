from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from api.serializers import (UserRegistrationSerializer,
                             UserLoginSerializer, 
                             UserProfileSerializer, 
                             UserChangePasswordSerializer,
                             SendPasswordResetEmailSerializer, 
                             UserPasswordResetSerializer)
from django.contrib.auth import authenticate
from api.renders import UserRender
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


# creating token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
@extend_schema(responses=UserRegistrationSerializer, request=UserRegistrationSerializer)
class UserRegistrationView(APIView):
    "implementing custom renderer to identify error with 'error' keyword"
    renderer_classes=[UserRender]
    def post(self, request):
        serializer= UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token= get_tokens_for_user(user)
        return Response({'toekn':token,'msg':'Registration successful'}, status=status.HTTP_201_CREATED)
      
        
@extend_schema(responses=UserLoginSerializer, request=UserLoginSerializer)
class UserLoginView(APIView):
    "accept user email and password"   
    renderer_classes=[UserRender]
    def post(self, request):
        serializer= UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email= serializer.data.get('email')
        password= serializer.data.get('password')
        user= authenticate(email=email, password= password)
        if user is not None:
            token= get_tokens_for_user(user)
            return Response({"token":token,"msg":"login success"},status=status.HTTP_200_OK)
        else:
            return Response({"errors":{"non field error":['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
       
    
# @extend_schema(
#     responses=UserProfileSerializer, 
#     request=UserProfileSerializer, 
#     )
class UserProfileView(APIView):
     "accept user token only from request based on token send profile "
     renderer_classes=[UserRender]
     permission_classes= [IsAuthenticated]
     def get(self,request,  id= None):
         serializer = UserProfileSerializer(request.user) #pass current user to serializer
         return Response(serializer.data)
     
@extend_schema(responses=UserChangePasswordSerializer, request=UserChangePasswordSerializer)
class UserChangePasswordView(APIView):
    "accept 2 password, user know their pass and wanna change it"   
    renderer_classes=[UserRender]
    permission_classes= [IsAuthenticated]
    def post(self, request):
        serializer= UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'password changed successfully'}, status=status.HTTP_200_OK)
  

@extend_schema(responses=SendPasswordResetEmailSerializer, request=SendPasswordResetEmailSerializer)
class SendPasswordResetEmailView(APIView):
    "forget password, accept user email" 
    renderer_classes=[UserRender]
    def post(self, request):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'password reset link sent. please check your email'}, status=status.HTTP_200_OK)
        
@extend_schema(responses=UserPasswordResetSerializer, request=UserPasswordResetSerializer)
class UserPasswordRestView(APIView):
    "use encoded uid + token "
    renderer_classes = [ UserRender]
    def post(self,request,uid, token ):
        serializer= UserPasswordResetSerializer(data= request.data , context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({"msg":"password reset successfully"}, status=status.HTTP_200_OK)
       