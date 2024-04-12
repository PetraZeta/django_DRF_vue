from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Worker, Work

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'], username=clean_data['username'])
        user_obj.save()
        return user_obj
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Worker
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model= Work
        fields = '__all__'