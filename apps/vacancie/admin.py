from django.contrib import admin
from apps.vacancie.models import Vacancie


class VacancieAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True


admin.site.register(Vacancie, VacancieAdmin)



