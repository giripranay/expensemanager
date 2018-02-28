from django.db import models
# Create your models here.


class table(models.Model):
    id=models.AutoField(primary_key=True)
    pub_dat=models.DateTimeField(auto_now=True)
    
    cost=models.IntegerField()


    categories = (
        ('FOOD','FOOD'),
        ('GROCERY','GROCERY'),
        ('PETROL','PETROL'),
        ('ENTERTAINMENT','ENTERTAINMENT'),
    )
    CATEGORY = models.CharField(choices=categories,max_length=25)
