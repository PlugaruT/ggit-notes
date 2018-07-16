from django.db import models


class Note(models.Model):
    title = models.TextField()
    date = models.DateField(auto_now=True)


class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='note_elements')