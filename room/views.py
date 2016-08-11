from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>You're at the Room index.</h1>")


def detail(request, room_id):
    return HttpResponse("<h1>Details for room %s</h1>" %(str(room_id)))
