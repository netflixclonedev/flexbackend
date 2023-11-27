from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Userdata
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
"""def index(request):
    return render(request,'common_app/index.html')
def login(request):
    return render(request,'common_app/login.html')
def signup(request):
    if request.method=='POST':
        useremail=request.POST['useremail']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=useremail).exists():
                messages.info(request,'E-mail_already_in_Use')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username_already_taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(email=useremail,username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password mismatched')
            return redirect('signup')
    else:
        return render(request,'common_app/signup.html')"""
def des(request):
    return render(request,'common_app/des.html')
def lpage(request):
    return render(request,"common_app/landingpage.html")
def create(request):
    return render(request,"common_app/createaccount.html")
def signin1(request):
    return render(request,"common_app/signin1.html")
def signin2(request):
    return render(request,"common_app/signin2.html")
def forgot(request):
    return render(request,"common_app/forgot.html")
def otp(request):
    return render(request,"common_app/otp.html")
def resetpassw(request):
    return render(request,"common_app/reset.html")