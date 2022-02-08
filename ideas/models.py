from django.db import models

# Create your models here.
IDEA_STATUS = (
    ("pending", "Waiting for review"),
    ("accepted", "Accepted"),
    ("done", "Done"),
    ("rejected", "Rejected"),
)

class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    status = models.CharField(choices=IDEA_STATUS, max_length=30, default="pending")

class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()
