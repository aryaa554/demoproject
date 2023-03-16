from django.db import models

# Create your models here.
class BizContact(models.Model):
    bizname = models.CharField(max_length=200)
    bizemail = models.EmailField()
    bizphone = models.CharField(max_length=200)
    

    def __str__(self):
        return self.bizname 
