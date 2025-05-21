from django.contrib import admin
from django.urls import path, include
from ads.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # логин, логаут, смена пароля
    path('accounts/register/', register, name='register'),   # регистрация
    path('', include('ads.urls')),
    path('api/', include('ads.api_urls')),
]