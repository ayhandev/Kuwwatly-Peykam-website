from django.contrib import admin
from .models import Client, Gallery, Photo

admin.site.register(Client)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'image')
    list_filter = ('gallery',)
