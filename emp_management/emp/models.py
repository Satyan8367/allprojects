from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    hire_date=models.DateField()
   

    def __str__(self):
        return '%s %s %s' %(self.first_name,self.last_name,self.role)
    
class personal_details(models.Model):
    first_name=models.CharField(max_length=50) 
    last_name=models.CharField(max_length=100)
    gmail=models.CharField(max_length=100)
    password=models.CharField(max_length=50)   
    def __str__(self):
        return '%s %s' %(self.first_name,self.gmail)

