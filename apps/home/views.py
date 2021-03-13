from django.shortcuts import render
from django.views.generic import ListView

from apps.home.models import Setting
from apps.cources.models import CategoryCourses
from apps.preimushestva.models import Advantage
from apps.testimonial.models import Testimonial
from apps.partner.models import Partners
from apps.teacher.models import Teacher
from apps.news.models import News



class HomeView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        advantage = Advantage.objects.all().order_by('-id')[:6]
        testimonial = Testimonial.objects.all().order_by('-id')[:5]
        partners = Partners.objects.all()
        teacher = Teacher.objects.all().order_by('-id')[:6]
        news = News.objects.all().order_by('-id')[:3]
        context = {
            'setting': setting,
            'testimonial': testimonial,
            'advantage': advantage,
            'cat_cour': cat_cour, 
            'partners': partners,
            'teacher':teacher,
            'news': news, 
        }
        return context


# def home(request):
#     setting = Setting.objects.get(pk=1)
#     cat_cour = CategoryCourses.objects.all()
#     advantage = Advantage.objects.all().order_by('-id')[:6]
#     testimonial = Testimonial.objects.all().order_by('-id')[:5]
#     partners = Partners.objects.all()
#     teacher = Teacher.objects.all().order_by('-id')[:6]
#     news = News.objects.all().order_by('-id')[:3]
#     context = {
#         'setting': setting,
#         'testimonial': testimonial,
#         'advantage': advantage,
#         'cat_cour': cat_cour, 
#         'partners': partners,
#         'teacher':teacher,
#         'news': news, 
#     }
#     return render(request, 'index.html', context)

