from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*

from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout 
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url="/Login/")
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_descri=data.get('receipe_descri')
        receipe_image=request.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_descri)
        print(receipe_image)
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_descri=receipe_descri,
            receipe_image=receipe_image,

        )
    
        return redirect('/receipes/')
    queryset=Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={'receipes':queryset}
    return render(request,'receipe.html',context)


@login_required(login_url="/Login/")
def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        
        receipe_name=data.get('receipe_name')
        receipe_descri=data.get('receipe_descri')
        receipe_image=request.FILES.get('receipe_image')
        
        queryset.receipe_name=receipe_name
        queryset.receipe_descri=receipe_descri
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipes/')
    context={'receipe':queryset}
    return render(request,'update.html',context)


@login_required(login_url="/Login/")
def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')
    
    
    
def Login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.info(request,"Invalid Username")
            return redirect('/Login/')
        
        
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Invalid Password")
            return redirect('/Login/')
        else:
            auth_login(request,user)
            return redirect('/receipes/')
        
    return render(request,'login.html')   

def logout_page(request):
    logout(request)
    return redirect('/Login/')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
           messages.info(request,"username is Already Taken")
           return redirect('/Register')
        user=User.objects.create(
            first_name=first_name,
        
            last_name=last_name,
            username=username,
            
        )
        
        user.set_password(password)
        user.save()
        messages.info(request,"The account Created Successfully")
        return redirect('/Register/')
    return render(request,'register.html')   

from django.core.paginator import Paginator
from django.db.models import Q,Sum
def student_page(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search) |
        Q(student_email__icontains=search) |
        Q(department__department__icontains=search) |
        Q(student_id__student_id__icontains=search)|
        Q(student_age__icontains=search)
        )
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'report/students.html',{'queryset':page_obj})


def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id )
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    print(total_marks)
    return render(request,'report/seemarks.html',{'queryset':queryset,'total_marks':total_marks})