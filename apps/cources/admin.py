from django.contrib import admin
from apps.cources.models import CategoryCourses


class CategoryCoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

admin.site.register(CategoryCourses, CategoryCoursesAdmin)