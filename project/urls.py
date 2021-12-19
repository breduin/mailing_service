"""project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import settings

# Заглушка для главной страницы сайта
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
# ===================================

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', current_datetime)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns