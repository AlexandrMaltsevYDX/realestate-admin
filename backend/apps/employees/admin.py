from django.utils.html import format_html
from django.contrib import admin
from apps.employees.models.profile import Profile, MediaModel, ProfileImages


class ProfileImagesInline(admin.TabularInline):
    model = ProfileImages
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [ProfileImagesInline]
    list_display = ("name", "display_media")

    def display_media(self, obj):
        media_instances = obj.profileimages_set.all().values_list(
            "media__attachment", flat=True
        )
        return ", ".join(str(attachment) for attachment in media_instances)

    display_media.short_description = "Media"

    readonly_fields = ("preview_image",)
    fieldsets = [
        ("Profile Details", {"fields": ["name", "preview_image"]}),
    ]

    def preview_image(self, obj):
        media_instances = obj.profileimages_set.all().values_list(
            "media__attachment", flat=True
        )
        return format_html(
            "<br>".join(
                '<img src="http://localhost/media/{}" height="50"/>'.format(attachment)
                for attachment in media_instances
            )
        )

    preview_image.short_description = "Media Preview"


@admin.register(MediaModel)
class MediaModelAdmin(admin.ModelAdmin):
    list_display = ("attachment", "preview_image")

    def preview_image(self, obj):
        return format_html('<img src="{}" height="50"/>'.format(obj.attachment.url))

    preview_image.short_description = "Preview"


@admin.register(ProfileImages)
class ProfileImagesAdmin(admin.ModelAdmin):
    list_display = ("profile", "media", "preview_image")

    def preview_image(self, obj):
        return format_html(
            '<img src="{}" height="50"/>'.format(obj.media.attachment.url)
        )

    preview_image.short_description = "Media Preview"
