from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group as BaseGroup
from apps.users.models import User, Group
from django.utils.translation import gettext_lazy as _


# Register your models here.
# Регистрировать юзеров
# Регестрировать прокси группу
# Отнаследоваться от верхних моделей.
# Отрегистрировать Группу
class CustomUserAdmin(UserAdmin):
    # Customize the UserAdmin as needed
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    exclude = ("username",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ("email",)


class CustomGroupAdmin(GroupAdmin):
    # Customize the GroupAdmin as needed
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)


admin.site.unregister(BaseGroup)
