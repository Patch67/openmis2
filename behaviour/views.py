from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>You're at the Behaviour index.</h1>")


def detail(request, behaviour_id):
    response = "<h1>Details for behaviour %s</h1>" %(str(behaviour_id))
    response += "<p>{{}}</p>"
    return HttpResponse(response)
