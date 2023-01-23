from rest_framework import serializers
from .models import Books
from django.contrib.auth import get_user_model

class BookSerilaizer(serializers.ModelSerializer):
    class Meta:    
        model = Books
        fields = '__all__'
class UserSerilaizer(serializers.ModelSerializer):
    class Meta:    
        model = get_user_model()
        fields =('id', "username")
