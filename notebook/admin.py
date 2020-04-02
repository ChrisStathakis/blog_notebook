from django.contrib import admin

from django.contrib import admin

from .models import Tags


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    pass
