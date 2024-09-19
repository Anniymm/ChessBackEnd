from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PersonalSpace

User = get_user_model()

class PersonalSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSpace
        fields = ['first_name', "last_name"] 
        read_only_fields = ['user'] # amas ro ver sheexos saertod, ro ar shecvalon 


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    personal_space = PersonalSpaceSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'confirm_password', 'personal_space']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data.get('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')  # valiodaciis dros ar minda es 

        # useris sheqmna 
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        # personalspacestvis minda calke shenaxva da sheqmna 
        PersonalSpace.objects.create(
            user=user,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()