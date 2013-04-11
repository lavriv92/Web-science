from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=155, blank=True)
    date_of_birthday = models.DateField()
    profile_picture_url = models.URLField()
    
    def __unicode__(self):
        return '%s' %self.user

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=155)
    #public_date = models.DateField()
    content = models.TextField()
    
    def __unicode__(self):
        return '%s' %self.title
