# Generated by Django 5.0.7 on 2024-08-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0003_alter_wanguser_email_alter_wanguser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanguser',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]
