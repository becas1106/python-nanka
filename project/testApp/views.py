from django.shortcuts import render

def index(request):
    return render(request, 'testApp/index.html')

def top(request):
    return render(request, 'testApp/top.html')
# Create your views here.
