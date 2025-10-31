from django.shortcuts import render
from .models import ExerciseProgress
from  user_exercises.models import UserExercises
from .serializers import ExerciseProgressSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
# Create your views here.

class ExerciseProgressViewSet(viewsets.ModelViewSet):
    queryset = ExerciseProgress.objects.all()
    serializer_class = ExerciseProgressSerializer
    
