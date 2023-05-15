
from django.forms import ModelForm
from .models import Faculty, Course, Student, ExamOffice, AR, Lecturer, Payment, Complaint
from django import forms



class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ExamofficeForm(forms.Form):
    Registration_number = forms.CharField(required=False)
    Paper_Code = forms.CharField(required=False)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('Registration_number', 'Faculty', 'Course', 'Current_Year', 'Email', 'Phone_Number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Course'].queryset = Course.objects.none()

        if 'Faculty' in self.data:
            try:
                faculty_id = int(self.data.get('Faculty'))
                self.fields['Course'].queryset = Course.objects.filter(Faculty_id=faculty_id).order_by('Course_Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['Course'].queryset = self.instance.Faculty.course_set.order_by('Course_Name')




class FileUploadForm(forms.Form):
    attachment = forms.FileField()
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('Registration_number','Complaint_type','Paper_Code','Paper_Name','Year_Of_Exam', 'Study_mode', 'Semester', 'Session')



class ARForm(forms.ModelForm):
    class Meta:
        model = AR
        fields = ( 'Faculty', 'Course', 'Lecturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Course'].queryset = Course.objects.none()
    
        if 'Faculty' in self.data:
            try:
                faculty_id = int(self.data.get('Faculty'))
                self.fields['course'].queryset = Course.objects.filter(Faculty_id=faculty_id).order_by('Course_Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['Course'].queryset = self.instance.Faculty.course_set.order_by('Course_Name')
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Lecturer'].queryset = Lecturer.objects.none()

        if 'Course' in self.data:
            try:
                course_id = int(self.data.get('Lecturer'))
                self.fields['Lecturer'].queryset = Lecturer.objects.filter(course_id=course_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['Lecturer'].queryset = self.instance.Course.Lecturer_set.order_by('Name')



class LecturerForm(ModelForm):
    class Meta:
        model = Lecturer
        fields = ('Name', 'Faculty', 'Course')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Course'].queryset = Course.objects.none()

        if 'Faculty' in self.data:
            try:
                faculty_id = int(self.data.get('Faculty'))
                self.fields['Course'].queryset = Course.objects.filter(Faculty_id=faculty_id).order_by('Course_Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['Course'].queryset = self.instance.Faculty.course_set.order_by('Course_Name')



"""
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

"""