from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'first_app/index.html')

# Create your views here.
