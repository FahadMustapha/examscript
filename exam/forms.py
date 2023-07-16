
from django.forms import ModelForm
from .models import Faculty, Course, AR, Lecturer, Complaint, Results, Accounts
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
import random, string

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password')
        

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


class ExamComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('Registration_number','Complaint_type','Paper_Code','Paper_Name','Year_Of_Exam', 'Study_System', 'Sem_Qter', 'Session', 'is_exam_office_approved')

class StoreComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('Registration_number','Complaint_type','Paper_Code','Paper_Name','Year_Of_Exam', 'Study_System', 'Sem_Qter', 'Session', 'is_store_approved')



class TrackForm(forms.Form):
    Track_code = forms.CharField(required=False)

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('Registration_number','Complaint_type','Paper_Code','Paper_Name','Year_Of_Exam', 'Study_System', 'Sem_Qter', 'Session')

    def generate_track_code(self):
        # Generate a unique track code
        characters = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(characters) for _ in range(10))
        while Complaint.objects.filter(track_code=code).exists():
            code = ''.join(random.choice(characters) for _ in range(10))
        return code

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.track_code = self.generate_track_code()
        instance.status = 'Pending'  # Set initial status
        if commit:
            instance.save()
        return instance
    



class ArComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('Registration_number','Complaint_type','Paper_Code','Paper_Name','Year_Of_Exam', 'Study_System', 'Sem_Qter', 'Session', 'is_ar_approved')

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


class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = '__all__'

class AccountsForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ('Registration_Number', 'Faculty', 'Course', 'Paper_Code','Paper_Name','Year', 'Study_System', 'Sem_Qter', 'Session', 'Complaint_type', 'Amount_Paid')


#users
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))    
    