
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.template import loader
from django.db.models import Q

from django.shortcuts import render, redirect
from exam.utils import render_to_pdf
from django.http import HttpResponse
from django.contrib import messages

from exam.forms import LoginForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from exam.forms import FacultyForm, CourseForm, StudentForm, ComplaintForm, ExamofficeForm, ARForm, LecturerForm, ResultsForm
from .models import Faculty, Course, Student, ExamOffice, Complaint, AR, Lecturer, Payment, Results

from datetime import timedelta
#redirects the user to login page after automatic session logout

AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=2),
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'The session has expired. Please login again to continue.',
}

# Create your views here.
@login_required(login_url='user-login')
def home_view(request):
    return render(request, 'home.html')

#Faculty form
@login_required
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

@login_required
def faculty_pdf_view(request):
    faculty = Faculty.objects.all()

    context = {
        'faculty': faculty
    }
    pdf = render_to_pdf("faculty/faculty_pdf.html", context)
    
    return HttpResponse(pdf, content_type = "application/pdf")

@login_required
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

@login_required
def delete_faculty_view(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    faculty.delete()
    message = "Deleted"
    return redirect(add_faculty_view)

#Course form
@login_required
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

@login_required
def course_pdf_view(request):
    course = Course.objects.all()

    context = {
        'course': course
    }
    pdf = render_to_pdf("course/course_pdf.html", context)

    return HttpResponse(pdf, content_type = "application/pdf")

@login_required
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


@login_required
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



@login_required
def complaint_view(request):
    message =""
    if request.method == "POST":
        complaint_form = ComplaintForm(request.POST, request.FILES)
        if complaint_form.is_valid():
            complaint_form.save()
            message="Your complaint has been submitted"

            complaint_form = ComplaintForm()
            
    else:
        complaint_form = ComplaintForm()

    messages.success(request, message)    

    complaint = Complaint.objects.all()

    context ={
        'form':complaint_form,
        'msg':message,
        'complaint':complaint, 
    }
    return render(request, "complaint/complaint.html", context)

@login_required
def complaint_details_view(request, complaint_id):
    message =""
    complaint = Complaint.objects.get(Complaint_id=complaint_id)

    if request.method == "POST":
        complaint_form = ComplaintForm(request.POST, instance= complaint)

        if complaint_form.is_valid():
            complaint_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)

    else:
        complaint_form = ComplaintForm(instance=complaint)
    
    context = {
        'form': complaint_form,
        'complaint': complaint,
        'msg': message,        
    }
    return render(request, "complaint/edit_complaint.html", context)


@login_required
def complaint_pdf_view(request):
    complaint = Complaint.objects.all()

    context = {
        'complaint': complaint
    }
    pdf = render_to_pdf("complaint/complaint_pdf.html", context)

    return HttpResponse(pdf, content_type = "application/pdf")



class ARCreateView(CreateView):
    model = AR
    form_class = ARForm
    success_url = reverse_lazy('ar_page')

class LecturerCreateView(CreateView):
    model = Lecturer
    form_class = LecturerForm
    success_url = reverse_lazy('lecturer_page')

def load_lecturers(request):
    course_id = request.GET.get('course')
    lecturers = Lecturer.objects.filter(Course_id=course_id).order_by('Name')
    return render(request, 'lecturers_dropdown.html', {'lecturers': lecturers})



class ResultsListView(ListView):
    model = Results
    context_object_name = 'people'
class ResultsCreateView(CreateView):
    model = Results
    form_class = ResultsForm
    success_url = reverse_lazy('results_add')
class ResultsUpdateView(UpdateView):
    model = Results
    form_class = ResultsForm
    success_url = reverse_lazy('results_changelist')
def load_courses(request):
    faculty_id = request.GET.get('faculty')
    courses = Course.objects.filter(Faculty_id=faculty_id).order_by('Course_Name')
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})


@login_required
def examoffice_view(request):

    form = ExamofficeForm(request.GET)
    queryset = Results.objects.all()

    if form.is_valid():
        regnumber = form.cleaned_data['Registration_number']
        code = form.cleaned_data['Paper_Code']
        
        if regnumber:
            queryset = queryset.filter(Registration_Number__icontains=regnumber)
        if code:
           queryset = queryset.filter(Paper_Code=code)

    complaint = Complaint.objects.all()

    context = {
        'form': form,
        'queryset': queryset,
        'complaint':complaint,
    }
    return render(request, 'examoffice.html', context)




#file upload view

def file_upload(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            Attachment = form.cleaned_data['Attachment']
            # Save the Attachment to the server
            with open('exam/uploads/' + Attachment.name, 'wb+') as destination:
                for chunk in Attachment.chunks():
                    destination.write(chunk)
            # Return a response to the user
            return render(request, 'complaint/complaint.html', {'success': True})
    else:
        form = ComplaintForm()
    return render(request, 'complaint/complaint.html', {'form': form})
#file upload view


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "registration/login.html", {"form": form, "msg": msg})

def sign_up_view(request):
    message = ""
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            message = "User created successfully"
            success = True
            return redirect("accounts/login.html")
            
        else:
            message = "Invalid Inputs"
        messages.success(request, message)

    else:
        sign_up_form = UserCreationForm()
    context = {
        'form': sign_up_form
    }
    return render(request, 'registration/register.html', context)



def register_user_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            #return redirect("accounts/login.html")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "./register.html", {"form": form, "msg": msg, "success": success})




 
"""
def index(request):  
    if request.method == 'POST':  
        worker = WorkersForm(request.POST, request.FILES)  
        if worker.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        worker = WorkersForm()  
        return render(request,"index.html",{'form':worker})  
    
        

def index(request):  
    if request.method == 'POST':  
        complaint = ComplaintForm(request.POST, request.FILES)  
        if complaint.is_valid():  
            handle_uploaded_file(request.FILES['Attachment'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        complaint = ComplaintForm()  
        return render(request,"complaint/complaint.html",{'form':complaint})  
    


"""

"""payment view
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
"""