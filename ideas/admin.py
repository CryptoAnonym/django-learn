from django.contrib import admin
from .models import Idea, Vote
from django.utils.html import format_html


# Register your models here.


class VoteInline(admin.TabularInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "show_youtube_url"]
    list_filter = ["status"]
    search_fields = ["title"]
    inlines = [
        VoteInline
    ]


    def show_youtube_url(self, obj):
        if len(obj.youtube_url) > 0:
            return format_html(f'<a href="{obj.youtube_url}" target="blank">{obj.youtube_url}</a>')
        else:
            return ""

    show_youtube_url.short_description = "Strona"


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["idea", "komentarz", "status"]
    list_filter = ["idea"]
