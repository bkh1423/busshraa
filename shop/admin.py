from django.contrib import admin
from .models import Product  # ولو عندك Category أو Order أضفها هنا كمان

# تسجيل الموديلات الخاصة بالمتجر
admin.site.register(Product)

