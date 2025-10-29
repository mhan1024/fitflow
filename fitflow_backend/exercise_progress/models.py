from django.db import models

import datetime

# Create your models here.
class ExerciseProgress(models.Model):
    # Foreign key reference to users table ?
    user_email = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    # Foreign key reference to user_exercises table
    user_exercise = models.ForeignKey('user_exercises.UserExercises', on_delete=models.CASCADE)
    
    date = models.DateField(auto_now_add=True)
    
    # strength progress
    weight_str = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    # kg, lbs
    weight_unit_str = models.CharField(null=True, blank=True, max_length=254) 
    
    # cardio progress
    time_car = models.TimeField(null=True, blank=True) 
    distance_car = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2) 
    dist_unit_car = models.CharField(null=True, blank=True, max_length=254) 
    incline_car = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2) 
    speed_car = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2) 
    speed_unit_car = models.CharField(null=True, blank=True, max_length=254) 

    # mobility progress
    duration_mob = models.TimeField(null=True, blank=True) 