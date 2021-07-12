# Generated by Django 3.2.5 on 2021-07-12 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='Unknown', max_length=50, verbose_name='نام محصول'),
        ),
    ]
