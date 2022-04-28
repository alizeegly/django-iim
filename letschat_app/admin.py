from django.contrib import admin

from letschat_app.models import Chat, Room


class ChatAdmin(admin.ModelAdmin):
    list_display = ("message", "username", 'get_room')

    def get_room(self, obj):
        return obj.room.name

admin.site.register(Room)
admin.site.register(Chat, ChatAdmin)