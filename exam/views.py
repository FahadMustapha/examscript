
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.template import loader
from django.db.models import Q
#for code generation
import random, string
from django.contrib.auth import get_user_model
from django.utils.datastructures import MultiValueDictKeyError

from django.shortcuts import render, redirect, get_object_or_404
from exam.utils import render_to_pdf
from django.http import HttpResponse
from django.contrib import messages

from exam.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from exam.forms import CustomUserCreationForm, ArComplaintForm, ExamComplaintForm, StoreComplaintForm
from exam.forms import FacultyForm, CourseForm, ComplaintForm, ExamofficeForm, ARForm, LecturerForm, ResultsForm, TrackForm
from .models import Faculty, Course, ExamOffice, Complaint, AR, Lecturer, Results, User

from datetime import timedelta
#redirects the user to login page after automatic session logout

AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=2),
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'The session has expired. Please login again to continue.',
}

# Create your views here.
@login_required()
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

def load_courses(request):
    faculty_id = request.GET.get('faculty')
    courses = Course.objects.filter(Faculty_id=faculty_id).order_by('Course_Name')
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})


"""Generate a random track code."""
def generate_track_code():
    """Generate a random track code."""
    length = 10
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

"""
tracking the status of the complaint
def track_complaint(request):
    if request.method == 'POST':
        track_code = request.POST.get('track_code')
        form = ComplaintForm(request.GET)

        if form.is_valid():
            code = form.cleaned_data['Track_code']
            
            #form = ComplaintForm(request.GET)  
            field = form['Track_code']  # Get the field by its name    
            queryset = Results.objects.all()#

            try:
                # Retrieve the complaint based on the provided track code
                complaint = Complaint.objects.get(track_code=track_code)

                # Render a response with the complaint status
                return render(request, 'complaint/complaint_status.html', {'complaint': complaint})

            except Complaint.DoesNotExist:
                # Handle case when the track code is not found
                return render(request, 'track_code_not_found.html')
        
    context = {
        'field': field
    }

    return render(request, 'complaint/track.html', context)
"""


@login_required
def complaint_view(request):
    message = ""
    if request.method == 'POST':
        complaint_form = ComplaintForm(request.POST)
        if complaint_form.is_valid():
            complaint = complaint_form.save()

            complaint_form = ComplaintForm()
            return render(request, 'messages/success.html', {'complaint': complaint})        
    else:
        complaint_form = ComplaintForm()
    complaint = Complaint.objects.all()

    context ={
        'form':complaint_form,
        'msg':message,
        'complaint':complaint,        
    }
    return render(request, "complaint/complaint.html", context)


@login_required
def track_complaint(request):
    trackform = TrackForm(request.GET)
    queryset = Complaint.objects.none()

    if trackform.is_valid():
        code = trackform.cleaned_data['Track_code']
                
        try:
            #__icontains
            complaint = Complaint.objects.get(track_code=code)
            #<span class="material-icons-outlined">done_outline</span>
            if complaint.is_exam_office_approved == "Pending":
                complaint.is_exam_office_approved = "Pending"
            elif complaint.is_exam_office_approved == "Rejected":
                complaint.is_exam_office_approved = "Rejected"
            elif complaint.is_exam_office_approved == "Approved":
                complaint.is_exam_office_approved = "Approved"
            
            complaint.save()
            queryset = [complaint]
        except Complaint.DoesNotExist:
            queryset = []


    context = {
        'form': trackform,
        'queryset': queryset,
        
    }#'filtered_complaints':filtered_complaints,
    return render(request, 'complaint/track.html', context)


    
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




def ar_view(request):
    if request.method == 'POST':
        form = ARForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ar_page')
    else:
        form = ARForm()
    filtered_complaints = Complaint.objects.filter(is_exam_office_approved="Pending", is_store_approved="Retrieved")
    context = {
        'form': form,
        'filtered_complaints': filtered_complaints        
        }
    return render(request, 'exam/ar_form.html', context)


#view for adding the is_ar_approved status tag, indicates that the ar has approved a certain complaint
def ar_data_view(request, complaint_id):
    message =""
    complaint = Complaint.objects.get(Complaint_id=complaint_id)

    if request.method == "POST":
        complaint_form = ArComplaintForm(request.POST, instance= complaint)
        if complaint_form.is_valid():
            complaint_form.save()

            complaint_form = ArComplaintForm()
            return render(request, 'messages/ar_success_message.html', {'complaint':complaint})
             
        else:
            message = "Entered invalid data"
        messages.success(request, message)
    else:
        complaint_form = ArComplaintForm(instance=complaint)
    
    context = {
        'form': complaint_form,
        'complaint': complaint,
        'msg': message,        
    }
    return render(request, 'exam/ar_complaint_data.html', context)

def ar_approved_view(request):
    filtered_complaints = Complaint.objects.filter(is_ar_approved="Approved")
    return render(request, 'exam/ar_approved.html', {'filtered_complaints':filtered_complaints})




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

    complaint = Complaint.objects.filter(is_exam_office_approved="")

    context = {
        'form': form,
        'queryset': queryset,
        'complaint':complaint,
    }
    return render(request, 'examoffice.html', context)

#view for adding the is_ar_approved status tag, indicates that the ar has approved a certain complaint
def exam_data_view(request, complaint_id):
    message =""
    complaint = Complaint.objects.get(Complaint_id=complaint_id)

    if request.method == "POST":
        complaint_form = ExamComplaintForm(request.POST, instance= complaint)
        if complaint_form.is_valid():
            complaint_form.save()

            complaint_form = ExamComplaintForm()
            return render(request, 'messages/exam_success_message.html', {'complaint':complaint})
             
        else:
            message = "Entered invalid data"
        messages.success(request, message)
    else:
        complaint_form = ExamComplaintForm(instance=complaint)
    
    context = {
        'form': complaint_form,
        'complaint': complaint,
        'msg': message,        
    }
    return render(request, 'exam/exam_complaint_data.html', context)

def pending_complaints_view(request):
    filtered_complaints = Complaint.objects.filter(is_exam_office_approved="Pending")
    return render(request, 'exam/exam_pending.html', {'filtered_complaints':filtered_complaints})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = ""
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("")
            else:
                msg = 'Invalid credentials'
        else:
            form.add_error(None, 'Invalid username or password')
    else:
       form = LoginForm()
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
        sign_up_form = UserCreationForm()        
    messages.success(request, message)

    context = {
        'form': sign_up_form
    }
    return render(request, 'registration/register.html', context)

User = get_user_model()
def create_user(request):
    if request.method == 'POST':
        try:
            Registration_Number = request.POST['Registration_Number']
            username = request.POST['Custom_username']
            password = request.POST['User_passcode']
            role = request.POST['role']

            if User.objects.filter(Custom_username=username).exists():
                return render(request, 'create_user.html', {'error_message': 'Username already exists.'})
            
            user = User.objects.create_user(Registration_Number=Registration_Number, Custom_username=username, User_passcode=password)

            if user == "Admin":
                user.is_superuser = True
            elif role == 'Student':
                user.is_student = True
            elif role == 'Examoffice':
                user.is_examoffice = True
            elif role == 'Registrar':
                user.is_ar = True
            elif role == 'Accounts':
                user.is_accounts = True
            elif role == 'Store':
                user.is_store = True

            user.save()
            redirect('user_created')
            return render(request, 'registration/user_created.html')
            
        except MultiValueDictKeyError:
            # Handle the case when 'role' key is not present
            role = None  # Set a default value or handle the error in an appropriate way

    users = User.objects.all() #just returning all users on the system

    context = {
        'users':users,
    }
    return render(request, 'create_user.html', context)


#Store views
@login_required
def store_view(request):
    form = ExamofficeForm(request.GET)
    queryset = Results.objects.all()
    if form.is_valid():
        regnumber = form.cleaned_data['Registration_number']
        code = form.cleaned_data['Paper_Code']
        
        if regnumber:
            queryset = queryset.filter(Registration_Number__icontains=regnumber)
        if code:
           queryset = queryset.filter(Paper_Code=code)
    else:
        form = ExamofficeForm()
    filtered_complaints = Complaint.objects.filter(is_exam_office_approved="Pending", is_store_approved="")

    context = {
        'form': form,
        'queryset': queryset,
        'filtered_complaints':filtered_complaints,
    }
    return render(request, 'exam/store.html', context)

def retrieved_script(request):
    filtered_complaints = Complaint.objects.filter(is_store_approved="Retrieved")
    return render(request, 'exam/retrieved.html', {'filtered_complaints':filtered_complaints})

#view for adding the is_ar_store status tag, indicates that the exam store has approved a certain complaint
def store_data_view(request, complaint_id):
    message =""
    complaint = Complaint.objects.get(Complaint_id=complaint_id)

    if request.method == "POST":
        complaint_form = StoreComplaintForm(request.POST, instance= complaint)
        if complaint_form.is_valid():
            complaint_form.save()

            complaint_form = StoreComplaintForm()
            return render(request, 'messages/store_success_message.html', {'complaint':complaint})
             
        else:
            message = "Entered invalid data"
        messages.success(request, message)
    else:
        complaint_form = StoreComplaintForm(instance=complaint)
    
    context = {
        'form': complaint_form,
        'complaint': complaint,
        'msg': message,        
    }
    return render(request, 'exam/store_complaint_data.html', context)
