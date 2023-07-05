from django.contrib import admin

# Register your models here.
from .models import Faculty, Course, Student, ExamOffice, Complaint, AR, Results


class facultyAdmin(admin.ModelAdmin):
    list_display = ("Faculty_Name", "Faculty_Coordinator")

admin.site.register(Faculty, facultyAdmin)


class courseAdmin(admin.ModelAdmin):
    list_display = ("Faculty", "Course_Name", "Course_Duration")
    
admin.site.register(Course, courseAdmin)


class studentAdmin(admin.ModelAdmin):
    list_display = ("Registration_number","Faculty", "Course","Current_Year","Email", "Phone_Number")

admin.site.register(Student, studentAdmin)


class complaintAdmin(admin.ModelAdmin):
    list_display = ("Complaint_id", "Date", "Registration_number", "Complaint_type", "Paper_Code", "Paper_Name","Year_Of_Exam", "Study_mode", "Semester", "Session", "Accounts_approval", "Exam_office_approval", "AR_approval", "Status", "Attachment")

admin.site.register(Complaint, complaintAdmin)


class examofficeAdmin(admin.ModelAdmin):
    list_display = ("Registration_Number", "Paper_Code")

admin.site.register(ExamOffice, examofficeAdmin)


class arAdmin(admin.ModelAdmin):
    list_display = ("Faculty", "Course","Lecturer")

admin.site.register(AR, arAdmin)


class resultsAdmin(admin.ModelAdmin):
    list_display = ("Registration_Number", "Faculty", "Course", "Paper_Code", "Paper_Name", "Year", "Study_mode", "Semester", "Session")

admin.site.register(Results, resultsAdmin)


