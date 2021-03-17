from django.contrib import admin
from apps.cources.models import CategoryCourses, Courses


class CategoryCoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

admin.site.register(CategoryCourses, CategoryCoursesAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

admin.site.register(Courses, CoursesAdmin)