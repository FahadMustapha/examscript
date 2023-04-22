
from django.forms import ModelForm
from .models import Faculty, Course, Student, Remark, ExamOffice
from django import forms



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('Registration_number', 'Faculty', 'Course', 'Current_Year', 'Email', 'Phone_Number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Course'].queryset = Course.objects.none()




class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

"""
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
"""
        
class RemarkForm(ModelForm):
    class Meta:
        model = Remark
        fields = '__all__'

class ExamOfficeForm(ModelForm):
    class Meta:
        model = ExamOffice
        fields = '__all__'