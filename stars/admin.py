from datetime import date
from django.contrib import admin, messages
from .models import Stars, Category


@admin.register(Stars)
class StarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brief_info', 'time_create', 'is_published')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    list_filter = ['cat__name', 'is_published']
    search_fields = ['name', 'cat__name']
    list_per_page = 20

    actions = ['set_published', 'set_draft']

    ordering = ['time_create', 'name']

    @admin.display(description='Возраст')
    def brief_info(self, stars: Stars):
        today = date.today()
        old = today.year - stars.birth_date.year
        if (stars.birth_date.month < today.month or
            (stars.birth_date.month == today.month and stars.birth_date.day <= today.day)):
            pass
        else:
            old -= 1
        return f'{old} лет'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Stars.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Stars.Status.DRAFT)
        self.message_user(request, f"{count} записи(ей) сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')