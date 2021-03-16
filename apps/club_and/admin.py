from django.contrib import admin
from apps.club_and.models import Club


class ClubAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


admin.site.register(Club, ClubAdmin)

