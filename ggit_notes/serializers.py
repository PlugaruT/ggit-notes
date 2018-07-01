from rest_framework import serializers
from ggit_notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Note
