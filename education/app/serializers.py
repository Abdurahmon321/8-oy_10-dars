from rest_framework import serializers
from .models import Student, Teacher, Course, Lesson, Homework, StudentHomework, Video, Attendance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class StudentHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHomework
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate_file(self, value):
        if value.size > 10 * 1024 ** 3:
            raise serializers.ValidationError("File size must be under 10 MB")
        if not value.name.endswith(('.mp4', '.mov', '.avi')):
            raise serializers.ValidationError("Invalid file type")
        return value


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
