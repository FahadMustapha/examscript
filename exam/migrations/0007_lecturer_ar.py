# Generated by Django 4.1.2 on 2023-05-02 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_remove_course_course_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.course')),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='AR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.course')),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.faculty')),
                ('Lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.lecturer')),
            ],
        ),
    ]