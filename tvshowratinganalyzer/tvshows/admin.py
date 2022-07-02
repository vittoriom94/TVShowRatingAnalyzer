from django.contrib import admin

from .models import Show, Episode


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
