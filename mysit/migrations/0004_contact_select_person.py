# Generated by Django 3.2.5 on 2021-07-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysit', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Select_Person',
            field=models.IntegerField(default=None, verbose_name='تعداد افراد'),
        ),
    ]