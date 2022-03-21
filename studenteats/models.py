from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=128,blank=True)
    telephone = models.CharField('Telephone',max_length=50,blank=True)
    birthday = models.DateTimeField('Last modified', auto_now=True)
    email = models.TextField(max_length=1000)
    university = models.CharField('university',max_length=50,blank=True)
    password = models.CharField(max_length=200)
    location = models.CharField('location',max_length=50,blank=True)
    role = models.CharField(max_length=20)
    picture= models.ImageField(upload_to="profile_image",blank=True)
    website= models.URLField(blank=True)
   
    def __str__(self):
        return self.name

class Recipe(models.Model):
    Recipe_ID =  models.IntegerField(default=0) 
    Title = models.CharField(max_length=128)
    Content = models.TextField(max_length=1000,blank=True)
    Tags = models.CharField(max_length=128,null=True)
    Cuisine=models.CharField(max_length=20)
    Created_Date=models.DateTimeField(blank=True, default=datetime.now)
    Owner=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Likes=models.IntegerField(default=0)

    def __str__(self): 
        return self.Title

class Deals(models.Model):
    Deal_ID=models.IntegerField(primary_key=True, default=0,unique=True)
    Name=models.CharField(max_length=128)
    Description=models.TextField(max_length=1000)
    Last_Date=models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Deals'
        
    def __str__(self): 
        return self.Name

class Restaurant(models.Model):
    Restaurant_ID=models.IntegerField(default=0,unique=True)
    Name=models.CharField(max_length=128)
    Description=models.TextField(max_length=1000)
    Tags=models.CharField(max_length=128)
    Cuisine=models.CharField(max_length=20)
    Owner=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Res_Deals=models.ForeignKey(Deals, null=True, blank=True,on_delete=models.CASCADE)
    Likes=models.IntegerField(default=0)
    Latitude = models.FloatField(default=0.0)
    Longitude = models.FloatField(default=0.0)
    Place = models.CharField(max_length=128, default='')
    
    class Meta:
        verbose_name_plural = 'restaurants'
    def __str__(self): 
        return self.Name

class Discussion(models.Model):
    Discussion_ID=models.IntegerField(default=0,unique=True)
    Title=models.CharField(max_length=128)
    Description=models.TextField(max_length=1000)
    Created_Time=models.DateTimeField()
    User_ID=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Views=models.IntegerField(default=0)
    Likes=models.IntegerField(default=0)
    
    def __str__(self): 
        return self.Title


class Discussion_Replies(models.Model):
    Description=models.TextField(max_length=1000)
    User_ID=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Created_Time=models.DateTimeField()
    Likes=models.IntegerField(default=0)
    Post_ID=models.IntegerField(default=0,unique=True)
    Discussion_ID=models.ForeignKey(Discussion, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Discussion replies'
    
    def __str__(self): 
        return self.Description


class Restaurant_Comments(models.Model):
    Description=models.TextField(max_length=1000)
    User_ID=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Created_Time=models.DateTimeField()
    Likes=models.IntegerField(default=0)
    Comment_ID=models.IntegerField(default=0,unique=True)
    Restaurant_ID=models.ForeignKey(Restaurant,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Restaurant comments'
        
    def __str__(self): 
        return self.Description


class Recipe_Comments(models.Model):
    Description=models.TextField(max_length=1000)
    User_ID=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    Created_Time=models.DateTimeField()
    Likes=models.IntegerField(default=0)
    Comment_ID=models.IntegerField(default=0,unique=True)
    Recipe_ID=models.ForeignKey(Recipe,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Recipe comments'
    
    def __str__(self): 
        return self.Description


#Admindetails only has one record that stores the details constant
#for a week to avoid same calculation again and again on each page refresh
class AdminDetails(models.Model):
    recipeWeek = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    restaurantWeek = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    beginnerVideo = models.URLField(default='https://www.youtube.com/watch?v=Mw-5pQBbZvA')
