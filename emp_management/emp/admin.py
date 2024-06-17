from django.contrib import admin

from emp.models import Employee,Role,Department,personal_details

# Register your models here.
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(personal_details)
