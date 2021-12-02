from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class contact(models.Model):
    name = models.CharField(_("نام"), max_length=50)
    email = models.EmailField(_("پست الکترونیکی"))
    subject = models.CharField(_("موضوع"), max_length=100)
    massage = models.TextField(_("پیام"))
    created_date = models.DateTimeField(_("زمان تولید"), auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(_("تاریخ بروز رسانی"), auto_now=True, auto_now_add=False)
    class Meta:
         ordering = ['-created_date']
    def __str__(self):
        return self.name
    