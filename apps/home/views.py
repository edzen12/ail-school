from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from apps.home.models import Setting
from apps.cources.models import CategoryCourses
from apps.preimushestva.models import Advantage
from apps.testimonial.models import Testimonial
from apps.partner.models import Partners
from apps.teacher.models import Teacher
from apps.gallery.models import Gallery
from apps.club_and.models import Club
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


class TeacherView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/teacher.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        teacher = Teacher.objects.all()
        cat_cour = CategoryCourses.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour, 
            'teacher': teacher
        }
        return context


class TeacherDetailView(View):
    def get(self, request, slug):
        teacher = Teacher.objects.get(slug=slug)
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        teacher_all = Teacher.objects.all().order_by('-id')[:5]
        context = {
            'teacher': teacher,
            'setting': setting,
            'cat_cour': cat_cour,
            'teacher_all': teacher_all
        }
        return render(request, "page_detail/teacher_detail.html", context)


class NewsView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/news.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        news = News.objects.all()
        cat_cour = CategoryCourses.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour, 
            'news': news
        }
        return context


class NewsDetailView(View):
    def get(self, request, slug):
        news = News.objects.get(slug=slug)
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        news_all = News.objects.all().order_by('-id')[:5]
        context = {
            'news': news,
            'setting': setting,
            'cat_cour': cat_cour,
            'news_all': news_all
        }
        return render(request, "page_detail/news_detail.html", context)


class GalleryView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/gallery.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        gallery = Gallery.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour, 
            'gallery': gallery
        }
        return context


class PartnerView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/partner.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        partners = Partners.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour, 
            'partners': partners
        }
        return context


class VacancieView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/vacancie.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour
        }
        return context


class UsloviyaView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/usloviya.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour
        }
        return context


class AboutView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour
        }
        return context


class ClubView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/club.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        club = Club.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour,
            'club': club
        }
        return context


class ClubDetailView(View):
    def get(self, request, slug):
        club = Club.objects.get(slug=slug)
        club_all = Club.objects.all().order_by('-id')[:5]
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        context = {
            'club': club,
            'setting': setting,
            'cat_cour': cat_cour,
            'club_all': club_all
        }
        return render(request, "page_detail/club_detail.html", context)


class ContactView(ListView):
    queryset = Setting.objects.get(pk=1)
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        setting = Setting.objects.get(pk=1)
        cat_cour = CategoryCourses.objects.all()
        context = {
            'setting': setting,
            'cat_cour': cat_cour
        }
        return context
