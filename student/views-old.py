from django.shortcuts import render, get_object_or_404
from .models import Student


def index(request):
    all_students = Student.objects.all()
    return render(request, 'student/index.html', {'all_students': all_students})


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student/detail.html', {'student': student})


def update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

