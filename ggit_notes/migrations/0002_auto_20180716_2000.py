# Generated by Django 2.0.7 on 2018-07-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ggit_notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.AddField(
            model_name='noteelement',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_elements', to='ggit_notes.Note'),
        ),
    ]