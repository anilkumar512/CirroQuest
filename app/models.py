from django.db import models
import os

# Create your models here.
class  UserModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.IntegerField()
    profile_picture = models.FileField(upload_to=os.path.join("static","profile_pictures"), null=True)
    profilename = models.CharField(max_length=100,null=True)
    coins =models.IntegerField(default=100)
    followers = models.IntegerField(default=0)
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'UserProfile'

class QuestionsModel(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=30)
    question = models.TextField(null= True)
    time = models.DateTimeField(null=True)

    def  __str__(self):
        return  self.name
    class Meta:
        db_table = 'QuestionsModel'


class AnswersModel(models.Model):
    qid = models.IntegerField(null=True)   
    email = models.EmailField(null=True)

    name = models.CharField(max_length=30)
    answers = models.TextField(null= True)
    time = models.DateTimeField(null=True)

    def  __str__(self):
        return  self.name
    class Meta:
        db_table = 'AnswersModel'


class FollowModel(models.Model):
    userid = models.IntegerField()
    email = models.EmailField(null=True)
    follow = models.IntegerField(default=0)

    def __str__(self):
        return self.email
    class Meta:
        db_table = 'FollowModel'