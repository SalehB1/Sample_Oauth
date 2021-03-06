# Generated by Django 4.0.3 on 2022-04-06 10:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'کاربری با آن نام کاربری از قبل وجود دارد.'}, help_text='هشدار نام کاربری باید بین 1 تا 15 حرف باشد و (فقط از حروف، اعداد و . / + / - / _ استفاده شود)', max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='نام کاربری باید حداقل یک حرف داشته باشد و @ پذیرفته نمی شود', regex='^[\\w.+-]*[a-zA-Z][\\w.+-]*\\Z')]),
        ),
    ]
