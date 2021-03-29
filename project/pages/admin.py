from django.contrib import admin
from admin_ordering.admin import OrderableAdmin
from .models import (
    Block,
    Page,
    Video,
    Audio,
    Text,
)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_file', 'subtitles', )


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('bitrate', )


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('text', )


class PageBlockInline(OrderableAdmin, admin.StackedInline):
    model = Block
    ordering_field = 'ordered'
    ordering_field_hide_input = True


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = (PageBlockInline, )
