from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,validators = [validate_password])
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','password','password2']
    
    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError("Password didn't match")
        return attrs
    

    def create(self, validated_data):
         validated_data.pop('password2')
         password = validated_data.pop('password')
         user = User(**validated_data)
         user.set_password(password)
         user.save()
         return user