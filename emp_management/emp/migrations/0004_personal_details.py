# Generated by Django 4.2.5 on 2023-12-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_remove_employee_gmail_remove_employee_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='personal_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('gmail', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
