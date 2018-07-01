from django.contrib import admin
from ggit_notes.models import Note
# Register your models here.


@admin.register(Note)
class Note(admin.ModelAdmin):
    pass
