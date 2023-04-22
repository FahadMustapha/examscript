
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from exam.utils import render_to_pdf
from django.http import HttpResponse
from django.contrib import messages
from exam.forms import FacultyForm, CourseForm, StudentForm, RemarkForm, ExamOfficeForm
from .models import Faculty, Course, Student

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

#Faculty form
def add_faculty_view(request):
    message =""
    if request.method == "POST":
        faculty_form = FacultyForm(request.POST)
        if faculty_form.is_valid():
            faculty_form.save()
            message="Faculty Added Successfully"
            
    else:
        faculty_form = FacultyForm()

    messages.success(request, message)    

    faculty = Faculty.objects.all()

    context ={
        'form':faculty_form,
        'msg':message,
        'faculty':faculty, 
    }
    return render(request, "faculty/add_faculty.html", context)

def faculty_pdf_view(request):
    faculty = Faculty.objects.all()

    context = {
        'faculty': faculty
    }
    pdf = render_to_pdf("faculty/faculty_pdf.html", context)
    
    return HttpResponse(pdf, content_type = "application/pdf")


def edit_faculty_view(request, faculty_id):
    message =""
    faculty = Faculty.objects.get(id=faculty_id)

    if request.method == "POST":
        faculty_form = FacultyForm(request.POST, instance= faculty)

        if faculty_form.is_valid():
            faculty_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)

    else:
        faculty_form = FacultyForm(instance=faculty)
    
    context = {
        'form': faculty_form,
        'faculty': faculty,
        'msg': message,        
    }
    return render(request, "faculty/edit_faculty.html", context)


def delete_faculty_view(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    faculty.delete()
    message = "Deleted"
    return redirect(add_faculty_view)

#Course form
def add_course_view(request):
    message =""
    if request.method == "POST":
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            message="Course Added Successfully"
            
    else:
        course_form = CourseForm()

    messages.success(request, message)    

    course = Course.objects.all()

    context ={
        'form':course_form,
        'msg':message,
        'course':course, 
    }
    return render(request, "course/add_course.html", context)

def course_pdf_view(request):
    course = Course.objects.all()

    context = {
        'course': course
    }
    pdf = render_to_pdf("course/course_pdf.html", context)

    return HttpResponse(pdf, content_type = "application/pdf")

def edit_course_view(request, course_id):
    message =""
    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        course_form = CourseForm(request.POST, instance= course)

        if course_form.is_valid():
            course_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)

    else:
        course_form = CourseForm(instance=course)
    
    context = {
        'form': course_form,
        'course': course,
        'msg': message,        
    }
    return render(request, "course/edit_course.html", context)


def delete_course_view(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    message = "Deleted"
    return redirect(add_course_view)
#Course form

"""
#Student Form
def student_view(request):
    message = ""
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            message="Student Added"
    else:
        student_form = StudentForm()

    messages.success(request, message)

    context ={
        'form':student_form,
        'msg' : message,
    }
    return render(request, "student.html", context)
"""


class StudentListView(ListView):
    model = Student
    context_object_name = 'people'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

def load_courses(request):
    faculty_id = request.GET.get('faculty')
    courses = Course.objects.filter(faculty_id=faculty_id).order_by('faculty_name')
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})


#Remark Form
def remark_view(request):
    message = ""
    if request.method == "POST":
        remark_form = RemarkForm(request.POST)
        if remark_form.is_valid():
            remark_form.save()
            message="Form submitted"
    else:
        remark_form = RemarkForm()

    messages.success(request, message)

    context ={
        'form':remark_form,
    }
    return render(request, "remark.html", context)


#Exam office Form
def examoffice_view(request):
    message = ""
    if request.method == "POST":
        examoffice_form = ExamOfficeForm(request.POST)
        if examoffice_form.is_valid():
            examoffice_form.save()
            message="Student Added"
    else:
        examoffice_form = ExamOfficeForm()

    messages.success(request, message)

    context ={
        'form':examoffice_form,
        'msg' : message,
    }
    return render(request, "examoffice.html", context)