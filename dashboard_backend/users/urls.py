from django.urls import path
from .views import signup_view, login_view, current_user, logout_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('me/', current_user, name='current'),
    path('logout/', logout_view, name='logout'),
]