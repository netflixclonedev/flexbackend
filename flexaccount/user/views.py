from django.shortcuts import render

# Create your views here.
#def index(request):
    #return render(request,'index.html')
def login(request):
    return render(request,'common_app/login.html')
def signup(request):
    return render(request,'common_app/signup.html')
