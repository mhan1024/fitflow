from django.db import models
import datetime

# Create your models here.
class UserExercises(models.Model):
    # Foreign key reference to users table ? 
    user_email = models.EmailField()
    
    # basic exercise details
    # strength, cardio, mobility
    category = models.CharField(max_length=254) 
    exercise_id = models.CharField() 
    exercise_name = models.CharField(max_length=254)
    gif_url = models.URLField()
    instructions = models.JSONField(default=list)
    # targetMuscles + secondaryMuscles
    target_muscles = models.JSONField(default=list) 
    date = models.DateField(auto_now_add=True)
    
    # strength exercise details
    weight_str = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    # kg, lbs
    weight_unit_str = models.CharField(null=True, blank=True, max_length=254) 
    sets_str = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2) 
    reps_str = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    
    # cardio exercise details
    # hh:mm:ss
    time_car = models.TimeField(null=True, blank=True) 
    distance_car = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2) 
    # mi, km, m
    dist_unit_car = models.CharField(null=True, blank=True, max_length=254) 
    # no units, just level
    incline_car = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2) 
    speed_car = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2) 
    # mph, km/h, min/mile, min/km
    speed_unit_car = models.CharField(null=True, blank=True, max_length=254) 
    
    # mobility exercise details
    # hh:mm:ss
    duration_mob = models.TimeField(null=True, blank=True) 
    sets_mob = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    reps_mob = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    # light, moderate, intense
    intensity = models.CharField(null=True, blank=True, max_length=254) 
    
    
    