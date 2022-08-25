from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.

def home(request):
    return render(request,'first_app/index.html')

def new_view(request):
    user_list = User.objects.order_by('name')
    user_dict = {'user_records':user_list}
    return render(request,'first_app/drugi.html', context=user_dict)