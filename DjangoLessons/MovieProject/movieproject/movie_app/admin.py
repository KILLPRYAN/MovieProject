from django.contrib import admin, messages
from .models import Movie, Director
from django.db.models import QuerySet


# Register your models here.
admin.site.register(Director)

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('40 to 59', 'Средний'),
            ('60 to 79', 'Высокий'),
            ('>= 80', 'Ультра')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == '40 to 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == '60 to 79':
            return queryset.filter(rating__gt=60).filter(rating__lt=80)
        if self.value() == '60 to 79':
            return queryset.filter(rating__lt=79)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['year']
    prepopulated_fields = {'slug': ('name',) }
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['rating']
    list_per_page = 3
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        # qs.update(currency=Movie.EUR)
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.ERROR
        )
