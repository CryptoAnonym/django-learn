from django.contrib import admin
from .models import Idea, Vote
# Register your models here.

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):