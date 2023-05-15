
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
    Registration_number = models.CharField(max_length=40)
    Faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    Current_Year = models.CharField(max_length=20, choices=YearOptions.choices)
    Email = models.EmailField(max_length=100)
    Phone_Number = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.Registration_number}"
#student modal class


class Complaint(models.Model):
    class YearOfExam(models.TextChoices):
        Year_1 = _('1')
        Year_2 = _('2')
        Year_3 = _('3')
        Year_4 = _('4')
        Year_5 = _('5')
    class studymode(models.TextChoices):
        DAY = _('DAY'),
        EVENING = _('EVENING'),
        WEEKEND = _('WEEKEND'),
    class type(models.TextChoices):
        Remark = _('Re-mark'),
        Missing_Marks = _('Missing marks'),
    class study(models.TextChoices):
        Semester = _('Semester'),
        Quarter = _('Quarter'),
    class list(models.TextChoices):
        Semester_1 = _('Semester1'),
        Semester_2 =_('Semester2'),
        Semester_3 =_('Semester3'),
        Semester_4 =_('Semester4'),
        Semester_5 =_('Semester5'),
        Semester_6 =_('Semester6'),
        Quarter_1 =_('Quarter1'),
        Quarter_2 =_('Quarter2'),
        Quarter_3 =_('Quarter3'),
        Quarter_4 =_('Quarter4'),
        Quarter_5 =_('Quarter5'),
        Quarter_6 =_('Quarter6'),
    class status(models.TextChoices):
        PENDING = _('Pending'),
        DONE = _('Done'),

    Complaint_id = models.CharField(max_length=20)
    Date = models.DateTimeField(verbose_name='Date Submitted', auto_now=True)
    Registration_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    Complaint_type = models.CharField(max_length=30, choices=type.choices)
    Paper_Code = models.CharField(max_length=30)
    Paper_Name = models.CharField(max_length=100)
    Year_Of_Exam = models.CharField(max_length=20, choices=YearOfExam.choices)

    Study_mode = models.CharField(max_length=30, choices=study.choices)
    Semester = models.CharField(max_length=30, choices=list.choices)

    Session = models.CharField(max_length=10, choices=studymode.choices)
    Accounts_approval = models.BooleanField()
    Exam_office_approval = models.BooleanField()
    AR_approval =models.BooleanField()
    Status = models.CharField(max_length=20, choices=status.choices)
    Attachment = models.FileField(upload_to='uploads/', null=True)



#exam office model
class ExamOffice(models.Model):
    Registration_Number = models.CharField(max_length=100)
    Paper_Code = models.CharField(max_length=20)


class Lecturer(models.Model):
    Name= models.CharField(max_length=150)
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{self.Name}"

class AR(models.Model):
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)


class Payment(models.Model):
    Transaction_code = models.CharField(max_length=50)
    Date = models.DateTimeField(auto_now=True)
    Registration_number = models.CharField(max_length=15)
    Phone_number = models.CharField(max_length=15)
    Reason = models.CharField(max_length=15)


