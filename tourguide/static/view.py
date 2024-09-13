from django.db import models

class restaurant(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="img")
    rating=models.FloatField()
    location=models.URLField(max_length=200)
    
    def __str__(self):
        return self.name

class hotel(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="img")
    rating=models.FloatField()
    location=models.URLField(max_length=200)
    
    def __str__(self):
        return self.name


class customer(models.Model):
    name = models.CharField(max_length=255)
    mobile=models.CharField(max_length=12)
    email = models.CharField(max_length=255)
    password=models.CharField(max_length=50,default="admin@123")
    
    def __str__(self):
        return self.name
