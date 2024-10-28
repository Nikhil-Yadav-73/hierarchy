from django.db import models
from django.contrib.auth.models import User

class State(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Bhakt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
    
class DistrictSevak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
    
class StateSevak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
    
    