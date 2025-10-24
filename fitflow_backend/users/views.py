from django.shortcuts import render
from firebase_admin import auth as firebase_auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import CustomUser
import json


# Create your views here.
@csrf_exempt
def auth_view(request):
    body = json.loads(request.body)
    id_token = body.get('idToken')
    
    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token.get('email')
        name = decoded_token.get('name')
        
        user, created = CustomUser.objects.get_or_create(
            display_name=name,
            email=email
        )
  
        return JsonResponse({"message": "Firebase login was successful", "email": user.email })
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=401)
    
