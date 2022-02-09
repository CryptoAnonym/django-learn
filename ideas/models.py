from django.db import models

# Create your models here.
IDEA_STATUS = (
    ("pending", "Waiting for review"),
    ("accepted", "Accepted"),
    ("done", "Done"),
    ("rejected", "Rejected"),
)

VOTE_STATUS = (
    ("Waiting for edit", "Waiting for edit"),
    ("PLUS", "PLUS"),
    ("MINUS", "MINUS"),
    ("INFO", "INFO"),
    ("QUESTION","QUESTION ")
)


class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    status = models.CharField(choices=IDEA_STATUS, max_length=30, default="pending")

    def __str__(self):
        return self.title


class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    komentarz = models.TextField()
    status = models.CharField(choices=VOTE_STATUS, max_length=30, default="Waiting for edit")

    def __str__(self):
        return f"ID: {self.id}"

