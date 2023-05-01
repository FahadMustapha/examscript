
from django.forms import ModelForm
from .models import Faculty, Course, Student, Remark, ExamOffice, SessionList
from django import forms

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


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ExamOfficeForm(ModelForm):
    class Meta:
        model = ExamOffice
        fields = '__all__'



class RemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ('Course_Code','Course_Name','Year_Of_Exam', 'Academic_session', 'Semester_l_Quarter', 'Session')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Semester_l_Quarter'].queryset = SessionList.objects.none()

        if 'StudySession' in self.data:
            try:
                studysession_id = int(self.data.get('StudySession'))
                self.fields['Semester_l_Quarter'].queryset = SessionList.objects.filter(studysession_id=studysession_id).order_by('Session_list')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Semester_l_Quarter'].queryset = self.instance.StudySession.sessionlist_set.order_by('Session_list')
