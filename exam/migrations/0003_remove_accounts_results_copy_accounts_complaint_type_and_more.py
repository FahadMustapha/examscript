# Generated by Django 4.1.2 on 2023-07-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_user_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='results_copy',
        ),
        migrations.AddField(
            model_name='accounts',
            name='Complaint_type',
            field=models.CharField(choices=[('Remark', 'Re-mark'), ('Missing_Marks', 'Missing marks')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Course',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Faculty',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Paper_Code',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Paper_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Registration_Number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accounts',
            name='Sem_Qter',
            field=models.CharField(choices=[('Semester_1', '1'), ('Semester_2', '2'), ('Semester_3', '3'), ('Semester_4', '4'), ('Semester_5', '5')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Session',
            field=models.CharField(choices=[('DAY', 'DAY'), ('EVENING', 'EVENING'), ('WEEKEND', 'WEEKEND')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Study_System',
            field=models.CharField(choices=[('Semester', 'Semester'), ('Quarter', 'Quarter'), ('Term', 'Term')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='Year',
            field=models.CharField(choices=[('Year_1', 'Year 1'), ('Year_2', 'Year 2'), ('Year_3', 'Year 3'), ('Year_4', 'Year 4'), ('Year_5', 'Year 5')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Custom_username',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Registration_Number',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
