from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signup_view(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not email or not password:
        return Response({'error': 'Missing username, email, or password'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    new_user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
    
    return Response({
        'first_name': new_user.first_name,
        'last_name': new_user.last_name,
        'email': new_user.email,
        'username': new_user.username
    })

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response({'error': 'Username and/or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
    
    refresh = RefreshToken.for_user(user)

    return Response({
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.get_username(),
        'access': str(refresh.access_token)
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    
    if user.is_authenticated:
        return Response({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.get_username()
        })
        
    return Response({'error': 'Not logged in'}, status=401)

@api_view(['POST'])
def logout_view(request):
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


    
