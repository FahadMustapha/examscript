# Generated by Django 4.1.2 on 2023-05-02 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_rename_semester_l_quarter_remark_semesterquarter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remark',
            old_name='Course_Code',
            new_name='Paper_Code',
        ),
        migrations.RenameField(
            model_name='remark',
            old_name='Course_Name',
            new_name='Paper_Name',
        ),
    ]
