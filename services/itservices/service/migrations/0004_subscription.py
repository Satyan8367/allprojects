# Generated by Django 4.2.5 on 2024-05-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_rename_admin_access_register_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('order_amount', models.IntegerField()),
                ('receipt', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
