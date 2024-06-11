from rest_framework import viewsets
from .models import Student, Teacher, Course, Lesson, Homework, StudentHomework, Video, Attendance
from .serializers import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class StudentHomeworkViewSet(viewsets.ModelViewSet):
    queryset = StudentHomework.objects.all()
    serializer_class = StudentHomeworkSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
