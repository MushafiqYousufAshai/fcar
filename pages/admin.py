from django.contrib import admin
from .models import Teams
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:50px" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('first_name', 'thumbnail', 'id')
    search_fields = ('first_name', 'designation',)
    list_filter = ('created_date',)


admin.site.register(Teams, TeamAdmin)

