# Generated by Django 3.2.10 on 2021-12-08 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210712_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=250, verbose_name='موضوع')),
                ('messages', models.TextField(verbose_name='پیام ها')),
                ('approved', models.BooleanField(default=False, verbose_name='حالت نمایش')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بروز رسانی')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='زمان تولید')),
                ('Poost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
