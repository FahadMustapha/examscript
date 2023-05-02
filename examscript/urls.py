

from django.contrib import admin
from django.urls import path, include
from exam.views import add_faculty_view, edit_faculty_view, delete_faculty_view, faculty_pdf_view
from exam.views import add_course_view, edit_course_view, delete_course_view, course_pdf_view
from exam.views import home_view, examoffice_view, payment_view

from django.views.generic import RedirectView
from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home_page"),
    path('examoffice/', examoffice_view, name="examoffice_page"),
    path('payment/', payment_view, name="payment_page"),

    path('list/', views.StudentListView.as_view(), name='student_changelist'),
    path('student/', views.StudentCreateView.as_view(), name='student_add'),
    path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),

    path('remark/', views.RemarkCreateView.as_view(), name='remark_page'),
    path('<int:pk>/', views.RemarkUpdateView.as_view(), name='remark_change'),
    path('ajax/load-sessions/', views.load_sessions, name='ajax_load_sessions'),
    
    path('faculty/add_faculty/', add_faculty_view, name="add_faculty_page"),
    path('faculty/edit_faculty/<int:faculty_id>/', edit_faculty_view, name="edit_faculty_page"),
    path('delete_faculty/<int:faculty_id>/', delete_faculty_view, name="delete_faculty_page"),
    path('faculty/faculty_pdf/', faculty_pdf_view, name="faculty_pdf_page"),

    path('course/add_course/', add_course_view, name="add_course_page"),
    path('course/edit_course/<int:course_id>/', edit_course_view, name="edit_course_page"),
    path('delete_course/<int:course_id>/', delete_course_view, name="delete_course_page"),
    path('course/course_pdf/', course_pdf_view, name="course_pdf_page"),

    path('ar/', views.ARCreateView.as_view(), name='ar_add'),
    path('<int:pk>/', views.ARUpdateView.as_view(), name='ar_change'),

    path('lecturer/', views.LecturerCreateView.as_view(), name='lecturer_page'),
]