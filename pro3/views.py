from django.http import HttpResponse
from django.shortcuts import render


def rend_demo(request):
    return render(request,"sample.html")