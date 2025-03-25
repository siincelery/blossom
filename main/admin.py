from django.contrib import admin

from main.models import Advantage

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title',) 