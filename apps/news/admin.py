from django.contrib import admin
from apps.news.models import News



class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


admin.site.register(News, NewsAdmin)