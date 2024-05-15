from .models import *
from  rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Student
            # fields = ["name", "age"]
            fields = '__all__'
            
        def validate(self, data):
            if data['age'] < 18:
               raise serializers.ValidationError({"error": "age must be greater than 18"})
           
            if data["name"]:
               for n in data["name"]:
                   if n.isdigit():
                      raise serializers.ValidationError({"error": "name cannot contain numbers"})
            return data