from django.contrib import admin
from pageTest.models import TypesOfPersonality, Question

@admin.register(TypesOfPersonality)
class TypesOfPersonalityAdmin(admin.ModelAdmin):
    list_display = ('name',) 

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type_of_personality')  # Поля, которые будут отображаться в списке
    list_filter = ('type_of_personality',)  # Фильтр по типу личности
    search_fields = ('text',)  # Поиск по тексту вопроса