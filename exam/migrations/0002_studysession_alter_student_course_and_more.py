# Generated by Django 4.1.2 on 2023-04-28 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudySession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Session_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.faculty'),
        ),
        migrations.CreateModel(
            name='SessionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Session_list', models.CharField(max_length=50)),
                ('Session_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.studysession')),
            ],
        ),
        migrations.AlterField(
            model_name='remark',
            name='Academic_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.studysession'),
        ),
        migrations.AlterField(
            model_name='remark',
            name='Semester_l_Quarter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.sessionlist'),
        ),
    ]
