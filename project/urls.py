"""project URL Configuration
"""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from . import settings


# Заглушка для главной страницы сайта
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
# ===================================


schema_view = get_schema_view(
    openapi.Info(
        title="Horeca API",
        default_version='v1',
        description="API сервисов",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    patterns=[path('api/', include('mailings.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
    )


urlpatterns = [
    path(
        'docs/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),    
    path('admin/', admin.site.urls),
    path('api/', include('mailings.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('', current_datetime)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
