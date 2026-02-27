from django.db import models
from django.core.validators import EmailValidator

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()]) 
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
