from rest_framework import serializers
from ggit_notes.models import Note, NoteElement


class NoteElementSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['note']
        model = NoteElement


class NoteSerializer(serializers.ModelSerializer):
    note_elements = NoteElementSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Note


    def create(self, validated_data):
        note_elements = validated_data["note_elements"]
        note = Note.objects.create(
            title = validated_data["title"]
        )

        for note_element in note_elements:
            NoteElement.objects.create(
                tag=note_element["tag"],
                content=note_element["content"],
                note=note
            )
        return note

    def update(self, instance, validated_data):
        note_elements = validated_data["note_elements"]

        instance.note_elements.all().delete()
        for note_element in note_elements:
            NoteElement.objects.create(
                tag=note_element["tag"],
                content=note_element["content"],
                note=instance
            )

        instance.save()

        return instance






