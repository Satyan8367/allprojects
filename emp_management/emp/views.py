from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail

from emp.models import Employee,Role,Department, personal_details

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=request.POST['phone']
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added succesfully")
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception Occured!")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove=Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("Employee removes successfully")
        except:
            return HttpResponse("Enter valid emp id")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role) 
        context={
            'emps':emps
        }   
        return render(request,'all_emp.html',context) 
    elif request.method=='GET':
        return render(request,'filter_emp.html')   
    else:   
        return HttpResponse("Exception occered!")
    

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gmail=(request.POST['gmail'])
        password=(request.POST['password'])
        phone=request.POST['phone']
        try:
           emp=Employee.objects.get(first_name=first_name,last_name=last_name)
           pd=personal_details(first_name=first_name,last_name=last_name,gmail=gmail,password=password)
           pd.save()
           return HttpResponse("signup successfully!")
        except: 
            return HttpResponse("Only employee can sign up!")  
    elif request.method=='GET':
        return render(request,'signup.html')
    else:
        return HttpResponse("An Exception Occured!")
    
def signin(request):
    if request.method=='POST':
        gmail=request.POST['gmail']
        password=request.POST['password'] 
        try:  
            pd=personal_details.objects.get(password=password) 
            fn=pd.first_name
            ln=pd.last_name
            # print(fn,ln)
            emps=Employee.objects.all()
            emps=emps.filter(first_name=fn,last_name=ln)
          
            context={
                'emps':emps
                }
            print(fn,ln)
            return render(request,'all_emp.html',context)
        except:
            return HttpResponse("only valid user can signin")
    elif request.method=='GET':
        return render(request,'signin.html')
    else:
        return HttpResponse("An Exception Occured!")  

from random import randint
def send_otp():
    s=''
    for i in range(6):
        s=s+str(randint(0,9))
    return s    

    
def forgot_password(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        gmail=request.POST['gmail']    
        try:
            pd=personal_details.objects.get(first_name=first_name,gmail=gmail)
            otp=send_otp()
            print(otp)
            send_mail('urgent mail','this is an important mail regarding your work'+otp,
              'satyan8367@gmail.com',[gmail])
            pd.password=otp
            print(otp)
            pd.save()
            return HttpResponse("otp send on your gmail")

        except:
            return HttpResponse("invalid")  
    elif request.method=='GET':
        return render(request,'forgot_password.html')
    else:
        return HttpResponse("An Exception Occured!")  
    
def change_password(request):
    if request.method=="POST":
        old_password=request.POST.get('old_password')
        new_password=request.POST.get('new_password')
        try:   
           pd=personal_details.objects.get(password=old_password)
           pd.password=new_password 
           pd.save()
           return HttpResponse("password change successfully")
        except:
            return HttpResponse("Invalid password")  
    elif request.method=='GET':
        return render(request,'change_password.html')
    else:
        return HttpResponse("An Exception Occured!")     
        
    

