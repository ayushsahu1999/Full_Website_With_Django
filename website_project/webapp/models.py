from django.db import models
from django.contrib.auth.models import User as Us
from django.urls import reverse



# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, related_name = 'webpages', on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("webapp:index")



class UserProfileInfo(models.Model):
    user = models.OneToOneField(Us, on_delete = models.CASCADE)
    # additional classes
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username
