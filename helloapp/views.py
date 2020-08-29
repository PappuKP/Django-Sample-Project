from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepageview(request):
    #  return HttpResponse("Welcome to Django")
    return render(request, 'home.html')


def aboutpageview(request):
    #  return HttpResponse("Welcome to About")
    return render(request, 'about.html')


def contactpageview(request):
    #  return HttpResponse("Welcome to Contact")
    return render(request, 'contact.html')
