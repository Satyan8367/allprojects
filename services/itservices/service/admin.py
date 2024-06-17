from django.contrib import admin

from service.models import Service,Register,Subscription

# Register your models here.
admin.site.register(Service)
admin.site.register(Register)
admin.site.register(Subscription)