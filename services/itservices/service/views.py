from django.shortcuts import render
from service.models import Register,Service
from django.http import JsonResponse

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models import Q
from django.core.mail import send_mail

from service.models import Register,Service,Subscription
import razorpay
from itservices.settings import RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET

# Create your views here.
def index(request):
    emps=Service.objects.all()
    context={
        'emps':emps
    }       
    return render(request,'index.html',context)

def payment_success(request):
    if request.method == "POST":
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            # Payment is successful
            # Update your database and send confirmation to the user
            return JsonResponse({'status': 'success'})
        except razorpay.errors.SignatureVerificationError:
            # Payment failed
            return JsonResponse({'status': 'failure'})

# home page for admin
def home(request):
    emps=Service.objects.all()
    context={
        'emps':emps
    }
    return render(request,'home.html',context)

# otp genration
from random import randint
def send_otp():
    s=''
    for i in range(6):
        s=s+str(randint(0,9))
    return s    
    

# register user
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        gmail=request.POST.get('gmail')  
        password=request.POST.get('password')
        otp=send_otp() 
        send_mail('Registration Otp','This is an important mail regarding your Registration'+otp,
              'satyan8367@gmail.com',[gmail])  
        reg=Register(name=name,gmail=gmail,otp=otp,password=password)
        reg.save()    
        return render(request,'otpconfirm.html')  
    elif request.method=='GET':
        return render(request,'register.html')
    else:
        return HttpResponse("An Exception Occured!") 
         
# otp confirmation
def otpconfirm(request):
    ot=request.POST.get('otp')
    try:
        data=Register.objects.get(otp=ot)
        if data.otp==ot:
            data.is_verify=True
            data.save()
            return redirect('index')
        else:
            return HttpResponse("Incorrect otp")
    except: 
        return HttpResponse("Incorrect otp")

  

# def login(request):
#     if request.method=='POST':
#         gmail=request.POST['gmail']
#         password=request.POST['password'] 
#         try:  
#             data=Register.objects.get(password=password,gmail=gmail) 
#             print(data.is_verify)
#             if data.is_verify:
#                 return render(request,'login.html',context)
#             else:
#                 return HttpResponse("Only verified user can login")    
#         except:
#             return HttpResponse("only valid user can signin")
#     elif request.method=='GET':
#         return render(request,'login.html')
#     else:
#         return HttpResponse("An Exception Occured!") 


def login(request):
    mail=request.POST.get('gmail')
    pwd=request.POST.get('password')

    amount = 50000  # amount in paise
    client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'payment': payment,
        'razorpay_key_id': RAZORPAY_KEY_ID,
        'amount': amount,
    }
    # client.set_app_details({"title" : "Django", "version" : "1.8.17"})
   
    # client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
    # client.set_app_details({"title" : "Django", "version" : "1.8.17"})

    # data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    # payment = client.order.create(data=data)
    # print(payment)
    # # {'id': 'order_ODNQ98KfDHxUBV', 'entity': 'order', 'amount': 500, 'amount_paid': 0, 'amount_due': 500, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1716345380} 
    # # print(payment.amount)
    # sub=Subscription(order_id=payment['id'],order_amount=payment['amount'],receipt=payment['receipt'],status=payment['status'])
    # sub.save()
    try:
        data=Register.objects.get(gmail=mail,password=pwd)
        print(data.is_verify)
        if data.is_verify=="True":
            emps=Service.objects.all()
            context={
                'emps':emps,
                "amount": 500,
                 "currency": "INR",
                  "receipt": "order_rcptid_11"
                }
            # if data.admin=="True":
            #     return render(request,'home.html',context)    
            # return JsonResponse('login successfully',safe=False)
            # client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
            # client.set_app_details({"title" : "Django", "version" : "1.8.17"})

            # data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
            # payment = client.order.create(data=data)
            # print(payment)
    # {'id': 'order_ODNQ98KfDHxUBV', 'entity': 'order', 'amount': 500, 'amount_paid': 0, 'amount_due': 500, 'currency': 'INR', 'receipt': 'order_rcptid_11', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1716345380} 
    # print(payment.amount)
            # sub=Subscription(order_id=payment['id'],order_amount=payment['amount'],receipt=payment['receipt'],status=payment        ['status'])
            # sub.save()
            return render(request,'indexhome.html',context)
        else:
            return JsonResponse('account is not verified' ,safe=False)
    except:
        return JsonResponse('either email or passward is incorrect',safe=False)   

def admin_access(request):
    mail=request.POST.get('gmail')
    pwd=request.POST.get('password')
    try:
        data=Register.objects.get(gmail=mail,password=pwd)
        print(data.is_verify)
        if data.is_verify=="True":
            emps=Service.objects.all()
            context={
                'emps':emps
                }
            if data.admin=="True":
                return render(request,'home.html',context)    
            # return JsonResponse('login successfully',safe=False)
            return render(request,'indexhome.html',context)
        else:
            return JsonResponse('account is not verified' ,safe=False)
    except:
        return JsonResponse('either email or passward is incorrect',safe=False)              

   

def createservice(request):
    if request.method=='POST':
        service_name=request.POST.get('service_name')
        payment_terms=request.POST.get('payment_terms')
        service_price=request.POST.get('service_price')
        service_package=request.POST.get('service_package')
        service_tax=request.POST.get('service_tax')
        service_image=request.POST.get('service_image')
        new_ser=Service(service_name=service_name,payment_terms=payment_terms,service_price=service_price,service_package=service_package,service_tax=service_tax,service_image=service_image)
        new_ser.save()
        # return HttpResponse("service Added successfully")
        return redirect('home')
    elif request.method=='GET':
        return render(request,'home.html')
    else:
        return HttpResponse("An Exception Occured!")


# def allservice(request):
#     emps=Service.objects.all()
#     context={
#         'emps':emps
#     }
#     return render(request,'allservice.html',context)




def edit(request):
    emps=Service.objects.all()
    context={
        'emps':emps
    }
    
    return redirect(request,'home.html',context)

def update(request,id):
    if request.method=="POST":
        service_name=request.POST.get('service_name')
        payment_terms=request.POST.get('payment_terms')
        service_price=request.POST.get('service_price')
        service_package=request.POST.get('service_package')
        service_tax=request.POST.get('service_tax')
        service_image=request.POST.get('service_image')
        new_ser=Service(id=id,service_name=service_name,payment_terms=payment_terms,service_price=service_price,service_package=service_package,service_tax=service_tax,service_image=service_image)
        new_ser.save()
        return redirect('home')
    
    
    return redirect(request,'home.html')

def delete(request,id):
    emps=Service.objects.filter(id=id).delete()
    context={
        "emps":emps
    }
    return redirect(request,'home.html',context)

# def view(request,id):
#     emps=Service.objects.filter(id=id)
#     context={
#         "emps":emps
#     }
#     return redirect(request,'view.html',context)



# from itservices.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
# client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
# order_amount=50000
# order_currency='INR'
# client.order.create(dict(amount=order_amount,currency=order_currency,payment_capture=1))
# print()
# # payment_order_id=payment_order['id']
# payment_order_id=1
# context={
#     "amount":100,
#     "api_key":RAZORPAY_API_KEY,
#     "order_id":payment_order_id
# }



    

   
    
                     


  
