from django.contrib import admin
from apps.about.models import AboutUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['one_big_title', 'one_big_image']
    save_on_top = True

admin.site.register(AboutUs, AboutUsAdmin)

