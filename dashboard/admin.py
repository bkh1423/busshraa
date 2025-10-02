from django.contrib import admin
from .models import Report  # ولو عندك Coupon أضفها هنا كمان

# تسجيل موديلات لوحة التحكم
admin.site.register(Report)

