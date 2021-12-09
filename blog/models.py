from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import gettext as _
# Create your models here.
class Category(models.Model):
    name = models.CharField(_("دسته بندی"), max_length=50)
    def __str__(self):
        return self.name
    
class post(models.Model):
    DRINKS = 'drinks'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    CHOICES = (
        (DRINKS, "drinks"),
        (LUNCH, "lunch"),
        (DINNER, "dinner"),
    )

    name = models.CharField(_("نام محصول"), max_length=50,default='Unknown')
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.SET_NULL, null= True)
    image = models.ImageField(_("عکس"), upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(_("عنوان"),max_length=255)
    content = models.TextField(_("مطالب"))
    tags=TaggableManager()
    Type_Food=models.CharField(_("نوع غذا"),max_length=50, choices=CHOICES,default='D')
    category = models.ManyToManyField(Category, verbose_name=_("دسته بندی"))
    countent_views = models.IntegerField(_("تعداد بازدید"),default=0)
    status = models.BooleanField(_("وضعیت"),default=False) 
    created_date = models.DateTimeField(_("زمان تولید"), auto_now_add=True)
    updated_date = models.DateTimeField(_("تاریخ بروز رسانی"), auto_now=True)
    published_date = models.DateTimeField(_("زمان انتشار"),null=False)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name

class comment(models.Model):
    Poost = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.CharField(_("نام"),max_length=255)
    email = models.EmailField(_("ایمیل"))
    subject = models.CharField(_("موضوع"),max_length=250)
    messages = models.TextField(_("پیام ها"),)
    approved = models.BooleanField(_("حالت نمایش"),default=False)
    update_date = models.DateTimeField(_("تاریخ بروز رسانی"),auto_now_add=True)
    created_date = models.DateTimeField(_("زمان تولید"),auto_now=True)

    def __str__(self):
        return self.name 
         
class Meta:
    ordreing = ['-created_date'] 

     