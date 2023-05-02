
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from exam.utils import render_to_pdf
from django.http import HttpResponse
from django.contrib import messages
from exam.forms import FacultyForm, CourseForm, StudentForm, RemarkForm, ExamOfficeForm, ARForm, LecturerForm, PaymentForm
from .models import Faculty, Course, Student, ExamOffice, Remark, SessionList, StudySession, AR, Lecturer, Payment

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


class StudentListView(ListView):
    model = Student
    context_object_name = 'people'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('remark_page')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

def load_courses(request):
    faculty_id = request.GET.get('faculty')
    courses = Course.objects.filter(Faculty_id=faculty_id).order_by('Course_Name')
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})


#Remark Form
class RemarkListView(ListView):
    model = Remark
    context_object_name = 'remark'

class RemarkCreateView(CreateView):
    model = Remark
    form_class = RemarkForm
    success_url = reverse_lazy('payment_page')

class RemarkUpdateView(UpdateView):
    model = Remark
    form_class = RemarkForm
    success_url = reverse_lazy('remark_page')

def load_sessions(request):
    studysession_id = request.GET.get('Academic_session')
    sessions = SessionList.objects.filter(Session_id=studysession_id).order_by('Session_list')
    return render(request, 'sessions_dropdown_list_options.html', {'sessions': sessions})


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

class ARCreateView(CreateView):
    model = AR
    form_class = ARForm
    success_url = reverse_lazy('ar_page')

class ARUpdateView(UpdateView):
    model = AR
    form_class = ARForm
    success_url = reverse_lazy('ar_changelist')


class LecturerCreateView(CreateView):
    model = Lecturer
    form_class = LecturerForm
    success_url = reverse_lazy('lecturer_page')


"""payment view"""
def payment_view(request):
    message = ""
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()
            message="Payment received"
    else:
        payment_form = PaymentForm()

    messages.success(request, message)

    context ={
        'form':payment_form,
        'msg' : message,
    }
    return render(request, "payment.html", context)

