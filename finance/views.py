from datetime import datetime
import datetime
from django.shortcuts import render,redirect
from finance.models import *
from user import *
from django.contrib import messages
from user.models import User
 
def bookings(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_id = request.user.id
            name = request.user.username
            email = request.user.email
            phone = request.user.phone
            checkin = request.POST["checkin"]
            checkout  = request.POST["checkout"]
            noad = request.POST["noad"]
            nokid = request.POST["nokid"]
            booking = request.POST["booking"]
            food = request.POST["food"]
            if checkin is not None:
                tra = Bookings.objects.create(user_id = user_id,name=name,email=email,phon=phone,checkin=checkin,checkout = checkout,noad = noad,nokid = nokid,booking = booking,food=food)
                tra.save()
                print("Booking is saved successfully")
                messages.info(request,"Booking saved successfully")
                return redirect('bookings')
        else:
            return render(request,'bookings.html')
    else:
        return render(request,'bookings.html')

def viewbook(request):
    if request.user.is_authenticated and request.user.is_staff:
        cred=Bookings.objects.all()
        email = User.objects.all()
 
        context ={
                'cred':cred,  
                'email':email,
            
            }
    else:
        cred=Bookings.objects.filter(user_id=request.user.id)
        email = User.objects.filter(id=request.user.id)
        context ={
                'cred':cred,  
                'email':email,
               
            }
    return render(request,'viewbook.html',context)


def deletebook(request,id):
    if request.user.is_authenticated:
        dcre=Bookings.objects.filter(id=id)
        dcre.delete()
        return redirect('viewbook')
    else:
        return render(request,'viewbook.html')

def home(request):
    return render(request,'home.html')


def blog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_id = request.user.id
            name = request.user.username
            title = request.POST["title"]
            content = request.POST["content"]
            
            
           
            if title is not None:
                tra = Blog.objects.create(user_id = user_id,author=name,title=title,content=content)
                tra.save()
                print("Blog is saved successfully")
                messages.info(request,"Blog saved successfully")
                return redirect('blog')
        else:
            return render(request,'blog.html')
    else:
        return render(request,'blog.html')

def viewblog(request):
    if request.user.is_authenticated and request.user.is_staff:
        blog=Blog.objects.all()
        
 
        context ={
                'blog':blog,  
               
            
            }
    else:
         blog=Blog.objects.all()
        
 
         context ={
                'blog':blog,  
               
            
            }
    return render(request,'view_blog.html',context)




   