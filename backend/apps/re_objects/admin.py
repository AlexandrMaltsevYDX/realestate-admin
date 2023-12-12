from django.utils.html import format_html
from django.contrib import admin
from apps.re_objects import (
    models,
)


class ReObjectMediaInline(admin.TabularInline):
    model = models.ReObjectMedia
    extra = 1


class ReObjectEngineeringServicesInline(admin.StackedInline):
    model = models.ReObjectEngineeringServices
    extra = 1


@admin.register(models.ReObject)
class ReObjectAdmin(admin.ModelAdmin):
    inlines = [ReObjectMediaInline, ReObjectEngineeringServicesInline]
    readonly_fields = ("display_media", "display_engineering_services")
    list_display = ("id", "display_media", "display_engineering_services")

    def display_media(self, obj):
        media_instances = obj.reobjectmedia_set.all().values_list(
            "media__attachment", flat=True
        )
        return format_html(
            "<br>".join(
                '<img src="http://localhost/media/{}" height="50"/>'.format(attachment)
                for attachment in media_instances
            )
        )

    def display_engineering_services(self, obj):
        engineering_services = obj.reobjectengineeringservices_set.all().values_list(
            "engineering_service__value", flat=True
        )
        return ", ".join(engineering_services)

    display_media.short_description = "Media"
    display_engineering_services.short_description = "Engineering Services"
