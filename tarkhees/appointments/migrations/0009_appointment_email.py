# Generated by Django 4.2.1 on 2023-07-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_remove_employee_email_remove_employee_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
