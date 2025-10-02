from django.contrib import admin
from django.urls import path, include  # نستورد include عشان نربط ملفات urls الخاصة بالتطبيقات

urlpatterns = [
   
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),   
    path('shop/', include('shop.urls')),           
    path('dashboard/', include('dashboard.urls')), 
]
