from django.db import models

import datetime

# Create your models here.
class ExerciseProgress(models.Model):
    # Foreign key reference to users table ?
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    # Foreign key reference to user_exercises table
    user_exercise = models.ForeignKey('user_exercises.UserExercises', on_delete=models.CASCADE)
        
    # strength progress
    weight_str = models.JSONField(null=True, blank=True, default=list)
    # kg, lbs
    weight_unit_str = models.CharField(null=True, blank=True, max_length=254) 
    
    # cardio progress
    time_car = models.JSONField(null=True, blank=True, default=list)
    distance_car = models.JSONField(null=True, blank=True, default=list) 
    dist_unit_car = models.CharField(null=True, blank=True, max_length=254) 
    incline_car = models.JSONField(null=True, blank=True, default=list) 
    speed_car = models.JSONField(null=True, blank=True, default=list)
    speed_unit_car = models.CharField(null=True, blank=True, max_length=254) 

    # mobility progress
    duration_mob = models.JSONField(null=True, blank=True, default=list)