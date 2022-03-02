from django.contrib import admin

from .models import Client
from .models import Mailing
from .models import Message


admin.site.register(Client)
admin.site.register(Mailing)
admin.site.register(Message)
