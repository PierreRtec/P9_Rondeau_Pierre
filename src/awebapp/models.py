from django.contrib import admin
from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    """User model."""

    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # exemple pour makemigrations et migrate une nouvelle colonne dans la BDD
    n_col = models.IntegerField(default=0)

    # exemple pour supprimer une colonne
    """
    username = None
    is_superuser = None
    """

class Ticket(models.Model):
    # Your Ticket model definition goes here
    pass


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    # Your UserFollows model definition goes here

    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow")

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )
    

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

