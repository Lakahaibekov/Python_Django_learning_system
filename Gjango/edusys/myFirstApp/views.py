from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse

from .sendSms import sendSms
from .models import Schedule, Groups, Courses, Time, Teacher, Student, Grades, Send


def home(request):
    courses = Courses.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'home.html', context)


def profile(request):
    return render(request, "teacher_page.html")


def teacher(request):
    courses = Courses.objects.all()
    groups = Groups.objects.all()
    schedule = Schedule.objects.all()
    time = Time.objects.all()

    return render(request, "teacher.html", {'courses': courses, 'groups': groups, 'schedule': schedule, 'time': time})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def grade(request, group_id):
    students = Student.objects.all().filter(group_id=group_id)
    grade = Grades.objects.all().filter(group_id=group_id).order_by("-date")
    kek = {
        'students': students,
        'grade': grade,
    }

    return render(request, 'grades.html', kek)


def set_grade(request, course_id, group_id, teacher_id, student_id):
    if request.method == 'POST':
        course = Courses.objects.get(pk=course_id)
        group = Groups.objects.get(pk=group_id)
        teacher = Teacher.objects.get(user_id=teacher_id)
        student = Student.objects.get(pk=student_id)
        newGrade = int(request.POST['grade'])
        try:
            grade = Grades.objects.get(course_id=course_id, group_id=group_id, teacher_id=teacher_id, student_id=student_id)
            grade.grade = newGrade
            grade.save()
        except:
            grade = Grades()
            grade.course = course
            grade.group = group
            grade.student = student
            grade.teacher = teacher
            grade.grade = newGrade
            grade.save()

    else:
        raise Http404("grade not found!")

    return HttpResponseRedirect(reverse('grade', args=(group_id,)))


def send_sms(request):
    print(request.method)
    if request.method == "POST":
        viewsName_st = request.POST.get("name_st")
        viewsName_tr = request.POST.get("name_sender")
        viewsName_cs = request.POST.get("name_course")
        viewsPhone = request.POST.get("phone")
        viewsGrade = request.POST.get("grade")
        print(viewsName_st, viewsName_tr, viewsPhone, viewsGrade)

        send = Send()
        send.name_student = viewsName_st
        send.name_teacher = viewsName_tr
        send.name_course = viewsName_cs
        send.grade_student = viewsGrade
        send.phone_student = viewsPhone
        send.save()
        sendSms(viewsName_st, viewsName_tr, viewsPhone, viewsGrade, viewsName_cs)
        return redirect("/teacher/")
    return render(request, "send.html", {})


def sms(request):
    return render(request, "send.html")











