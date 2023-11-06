from django.db import models

# Create your models here.
class brands(models.Model):

    def __str__(self):
        return self.brandsName
    
    brandsName = models.CharField(max_length=50)

