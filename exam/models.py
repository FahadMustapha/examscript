
# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Faculty(models.Model):
    Faculty_Name = models.CharField(max_length=200)
    Faculty_Coordinator = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Faculty_Name}"
    
class Course(models.Model):
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Course_Name = models.CharField(max_length=200)
    Course_Code = models.CharField(max_length=30)
    Course_Duration = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.Course_Name}"


class Student(models.Model):
    
    class YearOptions(models.TextChoices):
        Year_1 = _('1')
        Year_2 = _('2')
        Year_3 = _('3')
        Year_4 = _('4')
        Year_5 = _('5')
        Year_6 = _('6')
    
    Registration_number = models.CharField(max_length=20)
    Faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    Current_Year = models.CharField(max_length=20, choices=YearOptions.choices)
    Email = models.EmailField(max_length=100)
    Phone_Number = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Registration_number}"
#student modal class


class StudySession(models.Model):
    Session_name = models.CharField(max_length=40)
    def __str__(self):
        return self.Session_name
    

class SessionList(models.Model):
    Session = models.ForeignKey(StudySession, on_delete=models.CASCADE)
    Session_list = models.CharField(max_length=50)
    def __str__(self):
        return self.Session_list

class Remark(models.Model):
    class YearOfExam(models.TextChoices):
        Year_1 = _('1')
        Year_2 = _('2')
        Year_3 = _('3')
        Year_4 = _('4')
        Year_5 = _('5')

    class Sessions(models.TextChoices):
        DAY = _('DAY'),
        EVENING = _('EVENING'),
        WEEKEND = _('WEEKEND'),
    
    Course_Code = models.CharField(max_length=10)
    Course_Name = models.CharField(max_length=150)
    Year_Of_Exam = models.CharField(max_length=20, choices=YearOfExam.choices)
    Academic_session = models.ForeignKey(StudySession, on_delete=models.SET_NULL, null=True)
    Semester_l_Quarter = models.ForeignKey(SessionList, on_delete=models.SET_NULL, null=True)
    Session = models.CharField(max_length=10, choices=Sessions.choices)
    def __str__(self):
        return f"{self.Course_Name}"
#Remark modal class

#exam office model
class ExamOffice(models.Model):
    Registration_Number = models.CharField(max_length=100)
    