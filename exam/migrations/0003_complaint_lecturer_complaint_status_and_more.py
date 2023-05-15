# Generated by Django 4.1.2 on 2023-05-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_studysession_remove_sessionlist_study_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Lecturer',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaint',
            name='Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Semester',
            field=models.CharField(choices=[('Semester1', 'Semester 1'), ('Semester2', 'Semester 2'), ('Semester3', 'Semester 3'), ('Semester4', 'Semester 4'), ('Semester5', 'Semester 5'), ('Semester6', 'Semester 6'), ('Quarter1', 'Quarter 1'), ('Quarter2', 'Quarter 2'), ('Quarter3', 'Quarter 3'), ('Quarter4', 'Quarter 4'), ('Quarter5', 'Quarter 5'), ('Quarter6', 'Quarter 6')], max_length=30),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Study_mode',
            field=models.CharField(choices=[('Semester', 'Semester'), ('Quarter', 'Quarter')], max_length=30),
        ),
        migrations.DeleteModel(
            name='SessionList',
        ),
        migrations.DeleteModel(
            name='Studysession',
        ),
    ]