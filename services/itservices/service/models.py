from django.db import models

# Create your models here.
class Service(models.Model):
    service_name=models.CharField(max_length=50)
    payment_terms=models.CharField(max_length=100)
    service_price=models.IntegerField()
    service_package=models.CharField(max_length=100)
    service_tax=models.IntegerField()
    service_image=models.ImageField(upload_to ='service/')

    def __str__(self):
        return self.service_name

class Register(models.Model):
    name=models.CharField( max_length=50)    
    gmail=models.EmailField( max_length=254)
    otp=models.CharField( max_length=50)
    is_verify=models.CharField( max_length=50,default=False)
    password=models.CharField(max_length=50)
    admin=models.CharField( max_length=50,default=False)

    def __str__(self):
        return self.name

  

class Subscription(models.Model):
    order_id=models.CharField( max_length=50)
    order_amount=models.IntegerField()
    receipt=models.CharField( max_length=50)
    status=models.CharField( max_length=50)

