from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-&lpia9d=yy7)#xu4rb_erq%e-xg3&=(awnhos_m2)rc1!$0!h^'

DEBUG = True

ALLOWED_HOSTS = []


# ========================
# التطبيقات
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'accounts',
    'shop',
    'dashboard',
]


# ========================
# Middleware
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========================
# روابط المشروع
# ========================
ROOT_URLCONF = 'busshraa.urls'


# ========================
# القوالب
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # تعريف مجلد القوالب الرئيسي
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ========================
# WSGI
# ========================
WSGI_APPLICATION = 'busshraa.wsgi.application'


# ========================
# قاعدة البيانات
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ========================
# إعدادات كلمات المرور
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ========================
# اللغة والتوقيت
# ========================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# ========================
# الملفات الثابتة والوسائط
# ========================

# ملفات static (CSS, JS, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # أثناء التطوير
STATIC_ROOT = BASE_DIR / "staticfiles"     # عند استخدام collectstatic

# ملفات media (التي يرفعها المستخدم)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


# ========================
# الإعدادات الأخرى
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



