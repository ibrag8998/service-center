from django.contrib import admin
from django.contrib.admin import display

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    fields = [
        "subject",
        "description",
        "created_at",
        "expected_finished_at",
        "finished_at",
        "assignee",
        "client",
    ]
    readonly_fields = [
        "created_at",
        "finished_at",
    ]
    autocomplete_fields = ["assignee", "client"]
    list_display = [
        "__str__",
        "expected_finished_at",
        "is_finished",
        "assignee",
        "client",
    ]
    search_fields = ["subject", "description"]


admin.site.register(Order, OrderAdmin)
