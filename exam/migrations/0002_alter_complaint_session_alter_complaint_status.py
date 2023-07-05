# Generated by Django 4.1.2 on 2023-05-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Session',
            field=models.CharField(choices=[('DAY', 'Day'), ('EVENING', 'Evening'), ('WEEKEND', 'Weekend')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default=False, max_length=20),
        ),
    ]