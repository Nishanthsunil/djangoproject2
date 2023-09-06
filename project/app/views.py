from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth


def demo(request):
    if request.method== "POST":
        uname=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
            else:
                user=User.objects.create_user(username=uname,email=email,password=password)
                user.save()
        else:
            messages.info(request,"Password not matching")
            return redirect("/")
        return redirect("/")




    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('w')
        else:
            messages.info(request,"Invalid credential")
            return redirect("login")
    return render(request,'login.html')

def w(request):
    return HttpResponse("WELCOME")

# Create your views here.
