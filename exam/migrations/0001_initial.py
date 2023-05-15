# Generated by Django 4.1.2 on 2023-05-14 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=200)),
                ('Course_Duration', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExamOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Registration_Number', models.CharField(max_length=100)),
                ('Paper_Code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty_Name', models.CharField(max_length=200)),
                ('Faculty_Coordinator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_code', models.CharField(max_length=50)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Registration_number', models.CharField(max_length=15)),
                ('Phone_number', models.CharField(max_length=15)),
                ('Reason', models.CharField(max_length=15)),
            ],
        ),
        
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Registration_number', models.CharField(max_length=40)),
                ('Current_Year', models.CharField(choices=[('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4'), ('5', 'Year 5'), ('6', 'Year 6')], max_length=20)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=20)),
                ('Course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.course')),
                ('Faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.faculty')),
            ],
        ),

        migrations.CreateModel(
            name='Studysession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Study_mode', models.CharField(max_length=40)),
            ],
        ),

        migrations.CreateModel(
            name='SessionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semesters', models.CharField(max_length=50)),
                ('Study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.studysession')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.course')),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.faculty'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint_id', models.CharField(max_length=20)),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='Date Submitted')),
                ('Complaint_type', models.CharField(choices=[('Re-mark', 'Remark'), ('Missing marks', 'Missing Marks')], max_length=30)),
                ('Paper_Code', models.CharField(max_length=30)),
                ('Paper_Name', models.CharField(max_length=100)),
                ('Year_Of_Exam', models.CharField(choices=[('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4'), ('5', 'Year 5')], max_length=20)),
                ('Session', models.CharField(choices=[('DAY', 'Day'), ('EVENING', 'Evening'), ('WEEKEND', 'Weekend')], max_length=10)),
                ('Accounts_approval', models.BooleanField(null=True)),
                ('Exam_office_approval', models.BooleanField(null=True)),
                ('AR_approval', models.BooleanField(null=True)),
                ('Attachment', models.FileField(upload_to='uploads/')),
                ('Semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.sessionlist')),
                ('Registration_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.student')),
                ('Study_mode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.studysession')),
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
