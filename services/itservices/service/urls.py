"""
URL configuration for itservices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from service import urls
from service import views

from .views import home, payment_success

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register),
    path('otpconfirm',views.otpconfirm),
    path('login',views.login),
    path('admin_access',views.admin_access),
    path('createservice',views.createservice),
    path('home',views.home,name="home"),
    # path('deleteservice',views.deleteservice),
    # path('allservice',views.allservice),
    path('edit',views.edit,name="edit"),
    path('update/<str:id>',views.update,name="update"),
    path('delete/<str:id>',views.delete,name="delete"),
    # path('view/<str:id>',views.view,name="view"),
    # path('indexhome',views.indexhome,name="indexhome"),
    # path('payment',views.payment),
    # path('pay',views.pay,name="pay"),
    path('payment/success/', payment_success, name='payment_success'),
]
