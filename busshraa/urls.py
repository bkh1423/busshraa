from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views   # استدعاء ملف views.py اللي أضفناه في مجلد busshraa

urlpatterns = [
    # الصفحة الرئيسية
    path('', views.home, name='home'),

    # لوحة التحكم الافتراضية
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('dashboard/', include('dashboard.urls')),
]

# عرض ملفات static و media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

