from django.contrib import admin

from apps.news.models import News, Images


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['description']


admin.site.register(Images)