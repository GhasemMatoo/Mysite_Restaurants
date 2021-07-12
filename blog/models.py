from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Create your models here.
class Category(models.Model):
    name = models.CharField(_("دسته بندی"), max_length=50)
    def __str__(self):
        return self.name
    
class post(models.Model):
    name = models.CharField(_("نام محصول"), max_length=50,default='Unknown')
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.SET_NULL, null= True)
    image = models.ImageField(_("عکس"), upload_to='blog/',default='blog/default.jpg')
    title = models.CharField(_("عنوان"),max_length=255)
    content = models.TextField(_("مطالب"))
    #tag
    category = models.ManyToManyField(Category, verbose_name=_("دسته بندی"))
    countent_views = models.IntegerField(_("تعداد بازدید"),default=0)
    status = models.BooleanField(_("وضعیت"),default=False) 
    created_date = models.DateTimeField(_("زمان تولید"), auto_now_add=True)
    updated_date = models.DateTimeField(_("تاریخ بروز رسانی"), auto_now=True)
    published_date = models.DateTimeField(_("زمان انتشار"),null=False)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.title
    