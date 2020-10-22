from django.db import models

# Create your models here.
class RbtMusic(models.Model):
    RbtName= models.CharField(max_length=40)
    RbtSinger = models.CharField(max_length=40)
    RbtCode = models.IntegerField(max_length=10)
    RbtOwner = models.CharField(max_length=40)
    RbtCost = models.IntegerField(max_length=4)
    RbtDescription = models.CharField(max_length=100)
    RbtDate= models.DateField()
    def __str__ (self):
        return self.RbtSinger +" * " +self.RbtName + " * " + str(self.RbtCode)


class Singer(models.Model):
    SingerName = models.CharField(max_length=40)
    SingerBirthDay=models.DateField()
    def __str__ (self):
        return self.SingerName


class Owner(models.Model):
    OwnerName = models.CharField(max_length=40)
    def __str__(self):
        return self.OwnerName
