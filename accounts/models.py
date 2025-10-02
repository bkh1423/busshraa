from django.db import models

class Profile(models.Model):
    user_name = models.CharField("اسم المستخدم", max_length=100)
    email = models.EmailField("البريد الإلكتروني", unique=True)
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

    def __str__(self):
        return self.user_name


