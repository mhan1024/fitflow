from rest_framework import serializers
from .models import UserExercises

class UserExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExercises
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}  
        }