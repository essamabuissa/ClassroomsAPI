from rest_framework import serializers
from classes .models import Classroom
from django.contrib.auth.models import User


class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject','name','year','teacher']


class ClassroomDetailSerializer(serializers.ModelSerializer):
    class Meta:

        model = Classroom
        fields = ['id','subject','name','year','teacher']

class ClassroomUpdateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Classroom
        fields = ['subject','year','name']


class ClassroomCreateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Classroom
        fields = ['subject','year','name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password' ,'first_name' , 'last_name']

        def create(self, validate_data):
            username = validate_data['username']
            password = validate_data['password']
            firstname = validate_data['first_name']
            lastname = validate_data['last_name']
            user_obj = User(username = username , first_name = firstname , last_name = lastname)
            user_obj.set_password(password)
            user_obj.save()
            return validate_data
