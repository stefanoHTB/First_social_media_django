from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to = 'profile_images', blank=True, null=True, default='post_images/blankpicture.jpg')
    location = models.CharField(max_length=100, blank=True)
    

    def __str__(self):                      #observe from admin django 
        return self.user.username



class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100) #this is the person that is being follow 


    def __str__(self):
        return self.user 


        