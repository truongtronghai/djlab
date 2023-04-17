from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=50)
    sound = models.CharField(max_length=50)
        
    def __str__(self):
        return self.name

    def speak(self):
        return (self.name + " speaks " + self.sound)
    