from django.contrib import admin

from clients.models import Client


class ClientAdmin(admin.ModelAdmin):
    fields = ["full_name", "phone", "email"]
    list_display = ["full_name", "phone", "email"]
    search_fields = ["full_name", "phone", "email"]


admin.site.register(Client, ClientAdmin)
