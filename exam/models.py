
# Create your models here.
from django.db import models
#from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class User(AbstractUser):
    Registration_Number = models.CharField(max_length=50)
    Custom_username = models.CharField(max_length=30, null=False)
    User_passcode = models.CharField(max_length=30, null=False)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_examoffice = models.BooleanField(default=False)
    is_ar = models.BooleanField(default=False)  
    is_accounts = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    # Add any additional fields here

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


class Complaint(models.Model):    
    type=[("Remark", 'Re-mark'),
        ("Missing_Marks", 'Missing marks'), ]    
    YearOfExam=[("Year_1", 'Year 1'),
        ("Year_2", 'Year 2'),
        ("Year_3", 'Year 3'),
        ("Year_4", 'Year 4'),
        ("Year_5", 'Year 5') ]    
    studymode=[ ("DAY", 'DAY'),
        ("EVENING", 'EVENING'),
        ("WEEKEND", 'WEEKEND')  ]
    study=[ ("Semester", 'Semester'),
        ("Quarter", 'Quarter'),
        ("Term", 'Term'),]
    list=[("Semester_1", '1'),
        ("Semester_2", '2'),
        ("Semester_3", '3'),
        ("Semester_4", '4'),
        ("Semester_5", '5'),]
    status=[("Rejected", 'Rejected'),
        ("Approved", 'Approved'),]
    script=[  ("Not Found", 'Not Found'),
        ("Retrieved", 'Retrieved'),]
    approvals=[ ("Rejected", 'Rejected'),      
        ("Pending", 'Pending'),
        ("Complaint Resolved", 'Complaint Resolved')  ]
    to_registrar =[
        ("Send to Academic Registrar", "Send to Academic Registrar")    ]
    
    Complaint_id = models.IntegerField(primary_key=True)
    track_code = models.CharField(max_length=15, default=False, unique=True)
    Date = models.DateTimeField(verbose_name='Date Submitted', auto_now=True)
    Registration_number = models.CharField(max_length=30)
    Complaint_type = models.CharField(max_length=30, choices=type)
    Paper_Code = models.CharField(max_length=30)
    Paper_Name = models.CharField(max_length=100)
    Year_Of_Exam = models.CharField(max_length=20, choices=YearOfExam)
    Study_System = models.CharField(max_length=30, choices=study)
    Sem_Qter = models.CharField(max_length=30, choices=list)
    Session = models.CharField(max_length=10, choices=studymode, default=False)
    Assigned_Lecturer = models.CharField(max_length=90)
    is_exam_office_approved = models.CharField(max_length=30, choices=approvals)    
    is_store_approved =models.CharField(max_length=30, choices=script)
    to_ar = models.CharField(max_length=30, choices=to_registrar)
    is_ar_approved =models.CharField(max_length=30, choices=status)
    Complaint_resolved = models.CharField(max_length=30, choices=approvals)
    
    
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


class Results(models.Model):
    YearOfExam=[
        ("2018/2019", "2018/2019"),
        ("2019/2020", "2019/2020"),
        ("2020/2021", "2020/2021"),
        ("2021/2022", "2021/2022"),
        ("2022/2023", '2022/2023'),
        ("2023/2024", "2023/2024")
        ]  
    studymode=[
        ("DAY", 'DAY'),
        ("EVENING", 'EVENING'),
        ("WEEKEND", 'WEEKEND')   
        ]
    study=[
        ("Semester", 'Semester'),
        ("Quarter", 'Quarter'),
        ("Term", 'Term'),
        ]
    list=[
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
    ] 
    Date = models.DateTimeField(verbose_name='Date Submitted', auto_now=True)   
    Registration_Number = models.CharField(max_length=100)
    Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Paper_Code = models.CharField(max_length=30)
    Paper_Name = models.CharField(max_length=100)
    Score = models.IntegerField()
    Academic_Year = models.CharField(max_length=20, choices=YearOfExam)
    Study_System = models.CharField(max_length=30, choices=study)
    Sem_Qter = models.CharField(max_length=30, choices=list)
    Session = models.CharField(max_length=10, choices=studymode)
    Script_number = models.IntegerField(null=False)


class Accounts(models.Model):
    YearOfExam=[
        ("Year_1", 'Year 1'),
        ("Year_2", 'Year 2'),
        ("Year_3", 'Year 3'),
        ("Year_4", 'Year 4'),
        ("Year_5", 'Year 5')
        ]  
    studymode=[
        ("DAY", 'DAY'),
        ("EVENING", 'EVENING'),
        ("WEEKEND", 'WEEKEND')   
        ]
    study=[
        ("Semester", 'Semester'),
        ("Quarter", 'Quarter'),
        ("Term", 'Term'),
        ]
    type=[
        ("Remark", 'Re-mark'),
        ("Missing_Marks", 'Missing marks'),
    ]
    list=[
        ("Semester_1", '1'),
        ("Semester_2", '2'),
        ("Semester_3", '3'),
        ("Semester_4", '4'),
        ("Semester_5", '5'),
    ]
    Registration_Number = models.CharField(max_length=100, null=True)
    Faculty = models.CharField(max_length=100, null=True)
    Course = models.CharField(max_length=100, null=True)
    Paper_Code = models.CharField(max_length=30, null=True)
    Paper_Name = models.CharField(max_length=100, null=True)
    Year = models.CharField(max_length=20, choices=YearOfExam, null=True)
    Study_System = models.CharField(max_length=30, choices=study, null=True)
    Sem_Qter = models.CharField(max_length=30, choices=list, null=True)
    Session = models.CharField(max_length=10, choices=studymode, null=True)
    Complaint_type = models.CharField(max_length=10, default="Remark", null=False)
    Amount_Paid = models.IntegerField(null=False)
    Date = models.DateTimeField(verbose_name='Date Submitted', auto_now=True)
