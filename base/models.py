from django.db import models

# Create your models here.

class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=100)
    description = models.Textfield(null=True,blank=True)