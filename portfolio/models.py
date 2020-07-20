from django.db import models

class Project(models.Model):       #website dekhe dekhe ki ki ase & django model fiels
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')#INSTALL: pip install pillow
    url = models.URLField(blank=True)#blank=True applied to make it optional / disi jate kichu img elink thake r kichute jno na thake


    def __str__(self):    #better view in admin
        return self.title
