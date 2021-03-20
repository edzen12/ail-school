from django.contrib import admin
from apps.preimushestva.models import Advantage


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    save_on_top = True


admin.site.register(Advantage, AdvantageAdmin)

