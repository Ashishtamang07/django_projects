from api.models import User
from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.core.mail import send_mail

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta: 
        model = User
        fields = ['name', 'email', 'password','password2',  'tc']
    
    def validate(self, data):
        print("ln-13", data)
    
        if data['password'] != data['password2']:
    
            raise serializers.ValidationError("Passwords must match.")
    
        return data

    "we create custom model instace in serializer aftr"   
    def create(self, validated_data):
    
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length= 225)
    
    class Meta:
        model = User
        fields = ['email', 'password']
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'email', 'name']
class UserChangePasswordSerializer(serializers.ModelSerializer):
    "Field name `password2` is not valid for model `User`-> to resolve this error, declare password2 "
    "since password is the field name of user, so mention it directly in fields[]  "
    password2=serializers.CharField(max_length= 255, style={'input_type':'password'}, write_only= True)
    class Meta:
        model= User
        fields=['password', 'password2']
        
    " extarct user from context->if pass and pass2 match-> extract pass-> set user new pass"
    def validate(self, attrs):
        user= self.context.get('user')
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Password and confirm password don't match")
        password= attrs['password']
        user.set_password(password)
        user.save()
        return attrs


"if email exist validate"   
class SendPasswordResetEmailSerializer(serializers.Serializer):
    email= serializers.EmailField(max_length= 225)
    class Meta:
        fields = ['email']
        
    def validate(self, data):
       
        email=data.get('email')
        print(email)
        if User.objects.filter(email=email).exists():
            user= User.objects.get(email=email)
            uid= urlsafe_base64_encode(force_bytes(user.id))
            print("encode userid", uid)
            token= PasswordResetTokenGenerator().make_token(user)
            print('password reset toekn', token)
            link='http://localhost:3000/api/user/reset/' + uid+ '/'+ token 
            print(" password reset link", link)
        
            subject= "password reset link"
            message="click link to reset password " + link
            from_email="tamangashish314@gmail.com"
            to_email= user.email,
            send_mail(
                    "password reset link",
                    message,
                    "tamangashish314@gmail.com",
                    *[to_email],
                    
                )
            return data
        else:
            raise serializers.ValidationError("you are not a register user")
        
class UserPasswordResetSerializer(serializers.Serializer):
    """
    since, its not modelSerializer so, we need password and password2
    if its modelSerializer, we only need password2 coz password already existsin user model 
    """
    password=serializers.CharField(max_length= 255, style={'input_type':'password'}, write_only= True)
    password2=serializers.CharField(max_length= 255, style={'input_type':'password'}, write_only= True)
    class Meta:
        model= User
        fields=['password', 'password2']
        
    " extarct user from context->if pass and pass2 match-> extract pass-> set user new pass"
    def validate(self, attrs):
        try:
            user= self.context.get('user')
            uid= self.context.get('uid')
            token= self.context.get('token')
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError("Password and confirm password don't match")
            id= smart_str(urlsafe_base64_decode(uid))
            user= User.objects.get(id= id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is not valid or expired")
            password= attrs['password']
            user.set_password(password)
            user.save()
            return attrs
        except  DjangoUnicodeDecodeError as identifier:
               PasswordResetTokenGenerator().check_token(user, token)
               raise serializers.ValidationError("Token is not valid or expired")

