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
    
class UserProfile(models.Model):
    class Role(models.TextChoices):
        BHAGAT = 'bhagat', 'Bhagat'
        DISTRICT_SEVAKAR = 'district_sevakar', 'District Sevakar'
        STATE_SEVAKAR = 'state_sevakar', 'State Sevakar'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.BHAGAT
    )
    phone = models.CharField(max_length=10)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.user.username} -> {self.role}")
   