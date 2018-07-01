from django.db import models


class Note(models.Model):
    title = models.TextField()
    date = models.DateField(auto_now=True)
    content = models.TextField()
