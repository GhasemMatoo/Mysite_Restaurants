# Generated by Django 3.2.10 on 2021-12-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Type_Food',
            field=models.CharField(choices=[('drinks', 'drinks'), ('lunch', 'lunch'), ('dinner', 'dinner')], default='drinks', max_length=50, verbose_name='نوع غذا'),
        ),
    ]
