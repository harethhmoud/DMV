# Generated by Django 4.2.1 on 2023-07-23 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_employee_first_name_employee_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
    ]
