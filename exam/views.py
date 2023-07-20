
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.template import loader
from django.db.models import Q
#for code generation
import random, string

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.utils.datastructures import MultiValueDictKeyError

from django.shortcuts import render, redirect, get_object_or_404
from exam.utils import render_to_pdf
from django.http import HttpResponse
from django.contrib import messages

from exam.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from exam.forms import CustomUserCreationForm, ArComplaintForm, ExamComplaintForm, StoreComplaintForm, ExamComplaintResolvedForm, ExamToArForm
from exam.forms import FacultyForm, CourseForm, ComplaintForm, ExamofficeForm, ARForm, LecturerForm, ResultsForm, TrackForm, AccountsForm
from .models import Faculty, Course, ExamOffice, Complaint, AR, Lecturer, Results, User, Accounts

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
    filtered_complaints = Complaint.objects.filter(to_ar="Send to Academic Registrar", is_ar_approved="")
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


#Results views
@login_required
def add_results_view(request):
    message =""
    if request.method == "POST":
        results_form = ResultsForm(request.POST)
        if results_form.is_valid():
            results_form.save()
            message="Result Added Successfully"            
    else:
        results_form = ResultsForm()

    messages.success(request, message)    
    registration_number = request.GET.get('Registration_Number')
    paper_code = request.GET.get('Paper_Code')

    if registration_number and paper_code:
        results = Results.objects.filter(
            Q(Registration_Number=registration_number) & Q(Paper_Code=paper_code)
        )
    else:
        results = Results.objects.none()
    context ={
        'form':results_form,
        'msg':message,
        'results':results, 
    }
    return render(request, "results/results_form.html", context)

@login_required
def edit_results_view(request, results_id):
    message =""
    results = Results.objects.get(id=results_id)

    if request.method == "POST":
        results_form = ResultsForm(request.POST, instance= results)

        if results_form.is_valid():
            results_form.save()
            message = "Changes saved successfully"
            # return redirect('me')
            return render(request, 'messages/results_changes.html')
        else:
            message = "Entered invalid data"
        messages.success(request, message)

    else:
        results_form = ResultsForm(instance=results)
    
    context = {
        'form': results_form,
        'results': results,
        'msg': message,        
    }
    return render(request, "results/edit_results.html", context)

@login_required
def delete_results_view(request, results_id):
    results = Results.objects.get(id=results_id)
    results.delete()
    message = "Deleted"
    return redirect(add_results_view)


@login_required
def results_pdf_view(request):
    results = Results.objects.all()

    context = {
        'results': results
    }
    pdf = render_to_pdf("exam/results_pdf.html", context)
    
    return HttpResponse(pdf, content_type = "application/pdf")




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

#view for adding the is_exam_office_approved status tag, indicates that the exam office has approved a certain complaint
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

def exam_to_ar(request, complaint_id):
    message =""
    complaint = Complaint.objects.get(Complaint_id=complaint_id)

    if request.method == "POST":
        complaint_form = ExamToArForm(request.POST, instance= complaint)
        if complaint_form.is_valid():
            complaint_form.save()

            complaint_form = ExamToArForm()
            return render(request, 'messages/examtoar_success.html', {'complaint':complaint})
             
        else:
            message = "Entered invalid data"
        messages.success(request, message)
    else:
        complaint_form = ExamToArForm(instance=complaint)
    
    context = {
        'form': complaint_form,
        'complaint': complaint,
        'msg': message,        
    }
    return render(request, 'exam/exam_complaint_data.html', context)

def exam_new_results(request, complaint_id):
    message =""
    complaint = Complaint.objects.get(Complaint_id=complaint_id)

    if request.method == "POST":
        complaint_form = ExamComplaintResolvedForm(request.POST, instance= complaint)
        if complaint_form.is_valid():
            complaint_form.save()

            complaint_form = ExamComplaintResolvedForm()
            return render(request, 'messages/complaint_success_message.html', {'complaint':complaint})
             
        else:
            message = "Entered invalid data"
        messages.success(request, message)
    else:
        complaint_form = ExamComplaintResolvedForm(instance=complaint)
    
    context = {
        'form': complaint_form,
        'complaint': complaint,
        'msg': message,        
    }
    return render(request, 'exam/exam_complaint_data.html', context)



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
# def create_user(request):
#     if request.method == 'POST':
#         try:
#             registration_number = request.POST['Registration_Number']
#             password = request.POST['User_passcode']
#             role = request.POST['role']
#         except KeyError:
#             return render(request, 'create_user.html', {'error_message': 'Missing required fields.'})

#         if User.objects.filter(registration_number=registration_number).exists():
#             return render(request, 'create_user.html', {'error_message': 'Username already exists.'})

#         user = User.objects.create_user(registration_number=registration_number, User_passcode=password)

#         if role == 'Admin':
#             user.is_superuser = True
#         elif role == 'Student':
#             user.is_student = True
#         elif role == 'Examoffice':
#             user.is_examoffice = True
#         elif role == 'Registrar':
#             user.is_ar = True
#         elif role == 'Accounts':
#             user.is_accounts = True
#         elif role == 'Store':
#             user.is_store = True

#         user.save()

#         return redirect('user_created')

#     users = User.objects.all()
#     context = {'users': users}
#     return render(request, 'create_user.html', context)


def create_user(request):
    if request.method == 'POST':
        registration_number = request.POST.get('Registration_Number')
        username = request.POST.get('username')
        password = request.POST.get('User_passcode')
        role = request.POST.get('role')

        if User.objects.filter(Registration_Number=registration_number).exists():
            return render(request, 'create_user.html', {'error_message': 'Username already exists.'})

        user = User.objects.create_user(Registration_Number=registration_number, User_passcode=password)

        if role == 'Admin':
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

        return redirect('user_created.html')

    users = User.objects.all()
    context = {'users': users}
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
    filtered_complaints = Complaint.objects.filter(is_store_approved="Retrieved", to_ar="")
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

#Payment view
@login_required
def add_payments_view(request):
    message =""
    if request.method == "POST":
        payments_form = AccountsForm(request.POST)
        if payments_form.is_valid():
            payments_form.save()
            message="Payment recorded Successfully"            
    else:
        payments_form = AccountsForm()

    messages.success(request, message)    
    registration_number = request.GET.get('Registration_Number')
    paper_code = request.GET.get('Paper_Code')

    if registration_number and paper_code:
        payments = Accounts.objects.filter(
            Q(Registration_Number=registration_number) & Q(Paper_Code=paper_code)
        )
    else:
        payments = Accounts.objects.none()
    context ={
        'form':payments_form,
        'msg':message,
        'payments':payments, 
    }
    return render(request, "payment.html", context)

@login_required
def edit_payments_view(request, payment_id):
    message =""
    payment = Accounts.objects.get(id=payment_id)

    if request.method == "POST":
        payment_form = AccountsForm(request.POST, instance= payment)

        if payment_form.is_valid():
            payment_form.save()
            message = "Changes saved successfully"
        else:
            message = "Entered invalid data"
        messages.success(request, message)

    else:
        payment_form = AccountsForm(instance=payment)
    
    context = {
        'form': payment_form,
        'payment': payment,
        'msg': message,        
    }
    return render(request, "edit_payment.html", context)


@login_required
def payments_pdf_view(request):
    payments = Accounts.objects.all()

    context = {
        'payments': payments
    }
    pdf = render_to_pdf("payment_pdf.html", context)    
    return HttpResponse(pdf, content_type = "application/pdf")


@login_required
def delete_payments_view(request, payments_id):
    payments = Accounts.objects.get(id=payments_id)
    payments.delete()
    message = "Deleted"
    return redirect(add_payments_view)