from django.contrib import admin


# Register your models here.

from .models import Book, Hero


class HeroInline(admin.StackedInline):
    model = Hero
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'pub_date')
    list_filter = ['title']
    search_fields = ['title', 'price', 'pub_date']
    list_per_page = 100
    inlines = [HeroInline]


admin.site.register(Book, BookAdmin)


class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'content', 'book')
    list_filter = ['name', 'gender']
    search_fields = ['gender', 'name']
    list_per_page = 100


admin.site.register(Hero, HeroAdmin)


