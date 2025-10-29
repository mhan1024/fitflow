from .models import UserExercises
from .serializer import UserExercisesSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django.http import JsonResponse

import json
# Create your views here.

class UserExercisesViewSet(viewsets.ModelViewSet):
    queryset = UserExercises.objects.all()
    serializer_class = UserExercisesSerializer
    
    
    # Get exercises by email
    # http://localhost:8000/api/exercises/by-email/?user_email=EMAIL
    @action(detail=False, methods=['get'])
    def by_email(self, request):
        email = request.query_params.get('user_email')
        
        if not email:
            return JsonResponse({"error": "email parameter is required"})
        
        try:
            exercises = UserExercises.objects.filter(user_email=email)
            
            if not exercises.exists():
                return JsonResponse({"error": "no exercises found for user"})
            
            serializer = self.get_serializer(exercises, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        except Exception as e:
            return JsonResponse({"error": e}, status=status.HTTP_404_NOT_FOUND)
        
        
