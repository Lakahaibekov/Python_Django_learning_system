from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department_name = models.CharField(max_length=80)

    def __str__(self):
        return self.department_name


class Courses(models.Model):
    subject_name = models.CharField(max_length=200)
    department_name = models.OneToOneField(Department, on_delete=models.CASCADE)

    def __str__(self):
        id = str(self.pk)
        return self.subject_name + " | " + id


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.OneToOneField(Courses, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles_images', blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " | " + self.user.username


class Groups(models.Model):
    group_name = models.CharField(max_length=50)
    # group_dep = models.ForeignKey(Department, on_delete=models.CASCADE)
    group_course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles_images', blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " | " + self.user.username


class Grades(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return self.student.user.first_name + " " + self.student.user.last_name + " | " + self.course.subject_name


class Time(models.Model):
    time = models.CharField(max_length=80)

    def __str__(self):
        return self.time


class Schedule(models.Model):
    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = u'Schedule'
    group_id = models.ForeignKey(Groups, verbose_name='Group', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, verbose_name='Teacher', on_delete=models.CASCADE)
    time_id = models.ForeignKey(Time, verbose_name='Time', on_delete=models.CASCADE)
    DAYS_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
    )
    week_day1 = models.CharField(max_length=50, choices=DAYS_CHOICES, verbose_name='Days1')
    week_day2 = models.CharField(max_length=50, choices=DAYS_CHOICES, verbose_name='Days2')
    week_day3 = models.CharField(max_length=50, choices=DAYS_CHOICES, verbose_name='Days3')

    def __str__(self):
        return self.group_id


class Send(models.Model):
    name_student = models.CharField(max_length=50)
    name_teacher = models.CharField(max_length=50)
    name_course = models.CharField(max_length=50)
    grade_student = models.CharField(max_length=50)
    phone_student = models.CharField(max_length=50)

    def __str__(self):
        return self.name_student + " " + self.grade_student






