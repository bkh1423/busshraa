from django.db import models

class Report(models.Model):
    title = models.CharField("عنوان التقرير", max_length=200)
    generated_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)

    class Meta:
        verbose_name = "التقرير"
        verbose_name_plural = "التقارير"

    def __str__(self):
        return self.title


class Coupon(models.Model):
    code = models.CharField("كود الخصم", max_length=50, unique=True)
    discount = models.DecimalField("نسبة الخصم", max_digits=5, decimal_places=2)  # نسبة مئوية %
    active = models.BooleanField("فعال", default=True)

    class Meta:
        verbose_name = "الكوبون"
        verbose_name_plural = "الكوبونات"

    def __str__(self):
        return self.code

