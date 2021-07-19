from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('/')
    return render(request,'eco/signup.html')
def home(request):
    current_site = get_current_site(request)
    print(current_site)
    return render(request,'eco/home.html')
def userlogin(request):
    
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user:
            login(request, user)
        return redirect('/')
    return render(request,'eco/login.html')
def userlogout(request):
    logout(request)
    return redirect('/')

