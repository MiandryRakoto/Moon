from django.contrib import admin

from chat.models import Discussion, Message

# Register your models here.

admin.site.register(Discussion)
admin.site.register(Message)