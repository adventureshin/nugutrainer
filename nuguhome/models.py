from django.db import models
import random
# Create your models here.


class trainer(models.Model):
    gym = models.CharField(default='',max_length=20)
    name = models.CharField(default='',max_length=10)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    mapurl = models.TextField(default='')
    inform = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class score(models.Model):
    trainer_id = models.ForeignKey(trainer,on_delete=models.CASCADE)
    score = models.IntegerField(default=9)
    
    def __str__(self):
        return self.trainer_id
        
class gymlocation(models.Model):
    gym = models.TextField(default='')
    location = models.TextField(default='')
    
    def __str__(self):
        return self.gym