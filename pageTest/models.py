from django.db import models

class TypesOfPersonality(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип личности')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип личности'
        verbose_name_plural = 'Типы личности'

class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст вопроса')
    type_of_personality = models.ForeignKey(
        TypesOfPersonality,
        on_delete=models.CASCADE,
        verbose_name='Тип личности',
        related_name='questions'
    )
    weight = models.IntegerField(default=1, verbose_name='Вес вопроса')  # Добавляем вес вопроса

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'