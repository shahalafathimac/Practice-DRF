from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username','password']
        model = User

    def post(self,validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        user =authenticate(
            username = data["username"],
            password = data["password"],
        )

        if not user:
            raise serializers.errors({"register to login"})
        return user
