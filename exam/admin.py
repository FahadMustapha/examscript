from django.contrib import admin


# Register your models here.
from .models import Faculty, Course, ExamOffice, Complaint, AR, Results, User


admin.site.register(User)

class facultyAdmin(admin.ModelAdmin):
    list_display = ("Faculty_Name", "Faculty_Coordinator")
admin.site.register(Faculty, facultyAdmin)


class courseAdmin(admin.ModelAdmin):
    list_display = ("Faculty", "Course_Name", "Course_Duration")    
admin.site.register(Course, courseAdmin)


class studentAdmin(admin.ModelAdmin):
    list_display = ("Registration_number","Faculty", "Course","Current_Year","Email", "Phone_Number")


class complaintAdmin(admin.ModelAdmin):
    list_display = ("Complaint_id", "Date", "Registration_number", "Complaint_type", "Paper_Code", "Paper_Name","Year_Of_Exam", "Study_System", "Sem_Qter", "Session", "is_exam_office_approved", "is_ar_approved", "is_store_approved")
admin.site.register(Complaint, complaintAdmin)


class examofficeAdmin(admin.ModelAdmin):
    list_display = ("Registration_Number", "Paper_Code")
admin.site.register(ExamOffice, examofficeAdmin)


class arAdmin(admin.ModelAdmin):
    list_display = ("Faculty", "Course","Lecturer")
admin.site.register(AR, arAdmin)


class resultsAdmin(admin.ModelAdmin):
    list_display = ("Registration_Number", "Faculty", "Course", "Paper_Code", "Paper_Name", "Score", "Academic_Year", "Study_System", "Sem_Qter", "Session")
admin.site.register(Results, resultsAdmin)


