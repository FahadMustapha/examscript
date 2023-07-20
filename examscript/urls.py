

from django.contrib import admin
from django.urls import path, include
from exam.views import add_results_view, edit_results_view, delete_results_view, results_pdf_view
from exam.views import add_faculty_view, edit_faculty_view, delete_faculty_view, faculty_pdf_view
from exam.views import add_course_view, edit_course_view, delete_course_view, course_pdf_view
from exam.views import  examoffice_view, exam_to_ar, exam_new_results
from exam.views import add_payments_view, edit_payments_view, delete_payments_view, payments_pdf_view
from exam.views import home_view, complaint_view, complaint_pdf_view, complaint_details_view, track_complaint
from exam.views import create_user, ar_view, ar_data_view, exam_data_view, store_view, store_data_view
from exam.views import login_view, sign_up_view, retrieved_script, ar_approved_view, pending_complaints_view
from django.contrib.auth.views import LogoutView, LoginView

from django.views.generic import RedirectView
from exam import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_up/', sign_up_view, name="sign_up_page"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("", create_user, name="create_user_page"),

    path('home/', home_view, name="home_page"),

    path('examoffice/', examoffice_view, name="examoffice_page"),
    path('examdata/<int:complaint_id>/', exam_data_view, name="exam_display_page"),
    path('pendingcomplaints/', pending_complaints_view, name="pending_page"),
    path('examtoar/<int:complaint_id>/', exam_to_ar, name="exam_to_ar_page"),
    path('complaintresolved/<int:complaint_id>/', exam_new_results, name="resolved_page"),


    path('store/', store_view, name="store_page"),
    path('storedata/<int:complaint_id>/', store_data_view, name="store_display_page"),
    path('retrieved/', retrieved_script, name="retrieved_scripts"),

    path('a jax/load-courses/', views.load_courses, name='ajax_load_courses'),
    
    path('faculty/add_faculty/', add_faculty_view, name="add_faculty_page"),
    path('faculty/edit_faculty/<int:faculty_id>/', edit_faculty_view, name="edit_faculty_page"),
    path('delete_faculty/<int:faculty_id>/', delete_faculty_view, name="delete_faculty_page"),
    path('faculty/faculty_pdf/', faculty_pdf_view, name="faculty_pdf_page"),

    path('course/add_course/', add_course_view, name="add_course_page"),
    path('course/edit_course/<int:course_id>/', edit_course_view, name="edit_course_page"),
    path('delete_course/<int:course_id>/', delete_course_view, name="delete_course_page"),
    path('course/course_pdf/', course_pdf_view, name="course_pdf_page"),

    path('complaint/complaint/', complaint_view, name="complaint_page"),
    path('complaint/complaint_pdf/', complaint_pdf_view, name="complaint_pdf_page"),
    path('complaint/edit_complaint/<int:complaint_id>/', complaint_details_view, name="edit_complaint_page"),
    #track complaint
    path('complaint/track', track_complaint, name='tracking'),

    path('ar/', ar_view, name='ar_page'),
    path('ardata/<int:complaint_id>/', ar_data_view, name="ar_display_page"),
    path('arapproved/', ar_approved_view, name='ar_approved_page'),
    path('ajax/load-lecturers/', views.load_lecturers, name='ajax_load_lecturers'),

    path('lecturer/', views.LecturerCreateView.as_view(), name='lecturer_page'),

    path('results/', add_results_view, name='add_results_page'),
    path('results/edit_results/<int:results_id>/', edit_results_view, name="edit_results_page"),
    path('delete_results/<int:results_id>/', delete_results_view, name="delete_results_page"),
    path('exam/results_pdf/', results_pdf_view, name="results_pdf_page"),

    path('payment/', add_payments_view, name='add_payment'),
    path('edit_payment/<int:payment_id>/', edit_payments_view, name="edit_payment"),
    path('delete_payments/<int:payments_id>/', delete_payments_view, name="delete_payment"),
    path('payments_pdf/', payments_pdf_view, name="payments_pdf_page"),
]
