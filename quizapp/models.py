from django.db import models

# Create your models here.
class question(models.Model):
    qno=models.IntegerField()
    question=models.CharField(max_length=100)
    o1=models.CharField(max_length=100)
    o2=models.CharField(max_length=100)
    o3=models.CharField(max_length=100)
    o4=models.CharField(max_length=100)
    co=models.CharField(max_length=100)
    
    def __str__(self):
        return self.question


class fraud_model(models.Model):
    username = models.CharField(max_length=100)
    fraud = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username    
 
    


class leaderboard(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField()
    
    def __str__(self):
        return self.username    
 
    
