from django.contrib.postgres.fields import JSONField
from django.db import models

amenities= {
    "wifi": False,
    "swimming_pool": False,
    "fitness_center": False,
    "spa": False,
    "restaurant": False,
    "bar": False,
    "room_service": False,
    "parking": False,
    "pet_friendly": False,
    "ac": False,
    "tv": False,
    "laundry": False
}

class restaurant(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="restaurant")
    city=models.CharField(max_length=250)
    area=models.CharField(max_length=250)
    location=models.URLField(max_length=500)
    description=models.TextField(default="none")
    rating=models.FloatField(default=0)
    
    def __str__(self):
        return self.name


class hotel(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="hotel")
    city=models.CharField(max_length=250)
    area=models.CharField(max_length=250)
    location=models.URLField(max_length=500)
    description=models.TextField(default="none")
    amenities=models.JSONField(default=amenities )
    rating=models.FloatField(default=0)
    
    def __str__(self):
        return self.name
    
        

class place(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to="places")
    category=models.CharField(max_length=50)
    city=models.CharField(max_length=250)
    area=models.CharField(max_length=250)
    location=models.URLField(max_length=500)
    description=models.TextField(default="none")
    
    def __str__(self):
        return self.name
        

class customer(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    password=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class TourGuide(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="xyz")
    email = models.CharField(max_length=100, default="xyz")
    mobile = models.CharField(max_length=15, default="xyz")
    password = models.CharField(max_length=500, default="xyz")
    img = models.ImageField(upload_to="guide", default='guide/default_User_o.png')
    bio = models.TextField()
    languages = models.CharField(max_length=255)
    experience = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    price = models.CharField(max_length=25, default="1000")
    status = models.CharField( choices=STATUS_CHOICES, default='Inactive')
    rating=models.FloatField(default=0)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    bid=models.AutoField(primary_key=True)
    tid=models.ForeignKey(TourGuide, on_delete=models.CASCADE)
    cid=models.ForeignKey(customer, on_delete=models.CASCADE)
    pickup=models.CharField(max_length=50)
    venu=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    status=models.CharField(choices=STATUS_CHOICES, default='active')
    feedback=models.CharField(choices=STATUS_CHOICES, default='active')
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="NA")
    price=models.IntegerField(default=0)


class admins(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password=models.CharField(max_length=500)

    def __str__(self):
        return self.name
