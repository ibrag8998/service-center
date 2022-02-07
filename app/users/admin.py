from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import User


class ModifiedUserAdmin(UserAdmin):
    ...


admin.site.register(User, ModifiedUserAdmin)

admin.site.unregister(Group)
admin.site.site_header = "Сервисный центр"
admin.site.site_title = "Сервисный центр"
