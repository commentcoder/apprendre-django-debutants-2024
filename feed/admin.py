from django.contrib import admin
from feed.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']


admin.site.register(Message, MessageAdmin)
