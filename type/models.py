from django.db import models

# Create your models here.
class types(models.Model):

    def __str__(self):
        return self.typesName
    
    typesName = models.CharField(max_length=50)

