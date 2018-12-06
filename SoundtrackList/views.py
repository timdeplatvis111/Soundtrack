from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def results(request, soundtrackID):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % soundtrackID)

def detail(request, soundtrackID):
    return HttpResponse("You're looking at Soundtrack: %s." % soundtrackID)
