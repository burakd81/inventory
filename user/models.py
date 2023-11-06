from django.db import models

# Create your models here.
class users(models.Model):

    def __str__(self):
        return self.nameLastName
    
    nameLastName = models.CharField(max_length=50)

