from tkinter import CASCADE
from django.db import models


class User(models.Model):
    User_ID = models.IntegerField(default=0, unique=True)    
    Name = models.CharField(max_length=128)
    Email = models.TextField(max_length=1000)
    Password = models.CharField(max_length=200)
    Location = models.TextField(max_length=200)
    Role = models.CharField(max_length=20)
    Prfoile_Picture_Path = models.ImageField(upload_to="media",null=True)
    
    def __str__(self): 
        return self.Name


class Recipe(models.Model):
    Recipe_ID = models.IntegerField(default=0, unique=True) 
    Title = models.CharField(max_length=128)
    Content = models.TextField(max_length=1000,blank=True)
    Tags = models.CharField(max_length=128,null=True)
    Cuisine=models.CharField(max_length=20)
    Created_Date=models.DateTimeField()
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Likes=models.IntegerField(default=0)

    def __str__(self): 
        return self.Title


class Restaurant(models.Model):
    Restaurant_ID=models.IntegerField(default=0,unique=True)
    Name=models.CharField(max_length=10)
    Description=models.TextField(max_length=1000)
    Tags=models.CharField(max_length=128)
    Cuisine=models.CharField(max_length=20)
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Deals=models.TextField(max_length=200)
    Likes=models.IntegerField(default=0)
    
    def __str__(self): 
        return self.Name


class Deals(models.Model):
    Deal_ID=models.IntegerField(default=0,unique=True)
    Name=models.CharField(max_length=128)
    Discount=models.FloatField(default=0)
    Original_Price=models.FloatField(default=0)
    Description=models.TextField(max_length=1000)
    Last_Date=models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Deals'
        
    def __str__(self): 
        return self.Name

class Discussion(models.Model):
    Discussion_ID=models.IntegerField(default=0)
    Title=models.CharField(max_length=128)
    Description=models.TextField(max_length=1000)
    Created_Time=models.DateTimeField()
    User_ID=models.ForeignKey(User,on_delete=models.CASCADE)
    Likes=models.IntegerField(default=0)
    
    def __str__(self): 
        return self.Title


class Discussion_Replies(models.Model):
    Description=models.TextField(max_length=1000)
    User_ID=models.ForeignKey(User,on_delete=CASCADE)
    Created_Time=models.DateTimeField()
    Likes=models.IntegerField(default=0)
    Post_ID=models.IntegerField(default=0,unique=True)
    Discussion_ID=models.IntegerField(default=0,unique=True)

    class Meta:
        verbose_name_plural = 'Discussion replies'
    
    def __str__(self): 
        return self.Description


class Restaurant_Comments(models.Model):
    Description=models.TextField(max_length=1000)
    User_ID=models.ForeignKey(User,on_delete=CASCADE)
    Created_Time=models.DateTimeField()
    Likes=models.IntegerField(default=0)
    Comment_ID=models.IntegerField(default=0,unique=True)
    Restaurant_ID=models.ForeignKey(Restaurant,on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Restaurant comments'
        
    def __str__(self): 
        return self.Description


class Recipe_Comments(models.Model):
    Description=models.TextField(max_length=1000)
    User_ID=models.ForeignKey(User,on_delete=CASCADE)
    Created_Time=models.DateTimeField()
    Likes=models.IntegerField(default=0)
    Comment_ID=models.IntegerField(default=0,unique=True)
    Recipe_ID=models.ForeignKey(Recipe,on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Recipe comments'
    
    def __str__(self): 
        return self.Description