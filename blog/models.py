from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class post(models.Model):
    #image
    title = models.CharField(_("عنوان"),max_length=255)
    content = models.TextField(_("مطالب"))
    #tag
    #category
    countent_views = models.IntegerField(_("تعداد بازدید"),default=0)
    status = models.BooleanField(_("وضعیت"),default=False) 
    created_date = models.DateTimeField(_("زمان تولید"), auto_now_add=True)
    updated_date = models.DateTimeField(_("تاریخ بروز رسانی"), auto_now=True)
    published_date = models.DateTimeField(_("زمان انتشار"),null=False)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name
    