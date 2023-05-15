
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.template import loader
from django.db.models import Q
from django.shortcuts import render, redirect
from exam.utils import render_to_pdf
from django.http import HttpResponse
from django.contrib import messages

from exam.forms import FacultyForm, CourseForm, StudentForm, ComplaintForm, ExamofficeForm, ARForm, LecturerForm, FileUploadForm
from .models import Faculty, Course, Student, ExamOffice, Complaint, AR, Lecturer, Payment


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




def complaint_view(request):
    message =""
    if request.method == "POST":
        complaint_form = ComplaintForm(request.POST)
        if complaint_form.is_valid():
            complaint_form.save()
            message="Complaint Submitted Successfully"
            
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

def complaint_details_view(request, complaint_id):
    message =""
    complaint = Complaint.objects.get(id=complaint_id)

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
"""


def examoffice_view(request):

    student = Student.objects.all()
    #remark = Remark.objects.all()

    form = ExamofficeForm(request.GET)

    #if form.is_valid():        
     #   regnumber = form.cleaned_data['Registration_number']
      #  code = form.cleaned_data['Paper_Code']
        
       # if regnumber:
        #    queryset = queryset.filter(Registration_number__icontains=regnumber)
        #if code:
        #   queryset = queryset.filter(Paper_code=code)
    complaint = Complaint.objects.all()

    context = {
        'form': form,
        #'queryset': queryset,
        'complaint':complaint,
    }
    return render(request, 'examoffice.html', context)


#file upload view
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            # Save the file to the server
            with open('uploads/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # Return a response to the user
            return render(request, 'complaint/complaint.html', {'success': True})
    else:
        form = FileUploadForm()
    return render(request, 'complaint/complaint.html', {'form': form})