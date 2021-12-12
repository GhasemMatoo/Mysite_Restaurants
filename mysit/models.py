from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class contact(models.Model):
    name = models.CharField(_("نام"), max_length=50)
    email = models.EmailField(_("پست الکترونیکی"))
    subject = models.CharField(_("موضوع"), max_length=100)
    massage = models.TextField(_("پیام"))
    created_date = models.DateTimeField(
        _("زمان تولید"), auto_now=False, auto_now_add=True)
    updated_date = models.DateTimeField(
        _("تاریخ بروز رسانی"), auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Reservation(models.Model):
    BIRTH = 'birth'
    BUSINESS = 'busines'
    APPOINTMENT = 'appointment'
    PARTY = 'party'
    CHOICES = (
        (BIRTH, "birth"),
        (BUSINESS, "busines"),
        (APPOINTMENT, "appointment"),
        (PARTY, "party"),
    )
    name = models.CharField(_("نام"), max_length=50)
    email = models.EmailField(_("پست الکترونیکی"))
    subject = models.CharField(_("موضوع"), max_length=100)
    phone_number = models.CharField(_("شماره تلفن"), max_length=100)
    number_people = models.IntegerField(_("تعداداشخاص"),default=1)
    theme = models.CharField(_("تم"), max_length=50, choices=CHOICES, default='appointment')
    massage = models.TextField(_("پیام"))
    created_date = models.DateTimeField(_("زمان تولید"),auto_now_add=True)
    updated_date = models.DateTimeField(_("تاریخ بروز رسانی"), auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
