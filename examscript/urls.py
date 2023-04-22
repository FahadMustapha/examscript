"""examscript URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from exam.views import add_faculty_view, edit_faculty_view, delete_faculty_view, faculty_pdf_view
from exam.views import add_course_view, edit_course_view, delete_course_view, course_pdf_view
from exam.views import home_view, remark_view, examoffice_view

from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('remark/', remark_view, name="remark_page"),
    path('examoffice/', examoffice_view, name="examoffice_page"),

    path('', views.StudentListView.as_view(), name='student_changelist'),
    path('add/', views.StudentCreateView.as_view(), name='student_add'),
    path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),


    path('faculty/add_faculty/', add_faculty_view, name="add_faculty_page"),
    path('faculty/edit_faculty/<int:faculty_id>/', edit_faculty_view, name="edit_faculty_page"),
    path('delete_faculty/<int:faculty_id>/', delete_faculty_view, name="delete_faculty_page"),
    path('faculty/faculty_pdf/', faculty_pdf_view, name="faculty_pdf_page"),

    path('course/add_course/', add_course_view, name="add_course_page"),
    path('course/edit_course/<int:course_id>/', edit_course_view, name="edit_course_page"),
    path('delete_course/<int:course_id>/', delete_course_view, name="delete_course_page"),
    path('course/course_pdf/', course_pdf_view, name="course_pdf_page"),
]