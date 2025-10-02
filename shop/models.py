from django.db import models

class Category(models.Model):
    name = models.CharField("اسم الفئة", max_length=100)

    class Meta:
        verbose_name = "الفئة"
        verbose_name_plural = "الفئات"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("اسم المنتج", max_length=200)
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)

    class Meta:
        verbose_name = "المنتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField("اسم العميل", max_length=100)
    customer_email = models.EmailField("البريد الإلكتروني للعميل")
    created_at = models.DateTimeField("تاريخ الطلب", auto_now_add=True)
    total = models.DecimalField("إجمالي المبلغ", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "الطلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب {self.id} - {self.customer_name}"


