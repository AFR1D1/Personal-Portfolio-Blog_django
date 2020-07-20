from django.db import models
from django.urls import reverse

# Create your models here.
class Project2(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description= models.TextField()


    def __str__(self):            #better view in admin
        return self.title
