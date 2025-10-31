from rest_framework import serializers
from .models import ExerciseProgress

class ExerciseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseProgress
        fields = '__all__'