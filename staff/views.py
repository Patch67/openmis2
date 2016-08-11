from django.shortcuts import render, get_object_or_404
from .models import Staff


def index(request):
    all_staff = Staff.objects.all()
    return render(request, 'staff/index.html', {'all_staff': all_staff})


def detail(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    return render(request, 'staff/detail.html', {'staff': staff})
