# Generated by Django 4.2.5 on 2023-12-07 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_employee_gmail_employee_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
    ]
