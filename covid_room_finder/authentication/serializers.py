from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65,min_length=6,write_only=True)
    email=serializers.EmailField(max_length = 255)
    name=serializers.CharField(max_length=255)

    class Meta:
        model=User
        fields =['username','name','email']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email',('email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(validated_data)