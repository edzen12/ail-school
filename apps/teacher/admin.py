from django.contrib import admin
from apps.teacher.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True


admin.site.register(Teacher, TeacherAdmin)

