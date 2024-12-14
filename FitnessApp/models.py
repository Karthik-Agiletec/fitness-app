from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'account'
        
    user_type = models.CharField(blank=False, max_length=50)
    name = models.CharField(blank=False, max_length=50)
    contact = models.CharField(blank=False, max_length=50,unique=True)
    email = models.EmailField(blank=False, max_length=100, unique=True)  
    address = models.TextField(blank=True, default=None)  
    password = models.CharField(max_length=200, blank=True, default=None)
    is_active = models.IntegerField(default = 1)
    timestamp = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    class Meta:
        db_table='activity'
    activity_id=models.IntegerField()
    video_path=models.CharField(max_length=200)
    is_active=models.IntegerField(default="1")