from django.shortcuts import render,HttpResponse

# Create your views here.
def new(request):
    return HttpResponse("welcome")