from django.contrib import admin
from django.db import models
import datetime
from django.utils import timezone
<<<<<<< HEAD
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class UserFollows(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_by')
    confirm = models.CharField(max_length=128, blank=True)

    class Meta:
        unique_together = ('user', 'followed_user', )

    def __str__(self):
        return 'Suivis: ' + str(self.user) + " > " + str(self.followed_user)
=======

>>>>>>> e803522f7a10a37cdec6ad57e2b5db85a90e40a4

class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

