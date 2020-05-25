"""basket URL Configuration
"""
from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^api/v01/', include('core.urls')),
    re_path(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
