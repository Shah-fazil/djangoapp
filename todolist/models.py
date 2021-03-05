from django.db import models

# Create your models here.
class Todo(models.Model):
    
    item=models.CharField(max_length=20)
    cost=models.FloatField(null=True, blank=True, default=None)
    profit=models.FloatField(null=True, blank=True, default=None)
    datetime=models.DateField(auto_now_add=False,auto_now=False,blank=True)

    
        

 

    def __str__(self):
        return self.item