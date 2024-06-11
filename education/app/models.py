from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields as needed


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields as needed


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()


class StudentHomework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='homework_submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255)
    description = models.TextField()


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)  # Present or Absent
    date = models.DateField()
