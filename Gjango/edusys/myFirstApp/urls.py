from django.urls import path
from django.contrib.auth.views import auth_login
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', auth_login, name="login"),
    path("user/", views.profile, name="profile"),
    path("teacher/", views.teacher, name="teacher"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('grades/<int:group_id>', views.grade, name="grade"),
    path('grade/<int:course_id>/<int:group_id>/<int:teacher_id>/<int:student_id>', views.set_grade, name='set_grade'),
    path('send_sms/', views.send_sms, name='send_sms'),
    path('sms/', views.sms, name='sms')
]