from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    pass


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="followed_by"
    )
    followed_user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="followed_user"
    )

    def to_dict(self):
        return {"user": self.user, "followed_user": self.followed_user}

    class Meta:
        unique_together = (
            "user",
            "followed_user",
        )


class Ticket(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="static/awebapp/images/")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} by {}".format(self.title, self.user)


class Review(models.Model):

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="review")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.ticket.title, self.headline)
