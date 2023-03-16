from django.db import models

# Create your models here.
class BizCont(models.Model):
    name1 = models.CharField(max_length=200)
    email1 = models.EmailField()
    phone1 = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name 
