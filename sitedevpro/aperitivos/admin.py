from django.contrib.admin import ModelAdmin, register

from sitedevpro.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'youtube_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('titulo', )}
