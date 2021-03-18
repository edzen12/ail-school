from django.urls import path
from apps.home import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('gallery/', views.GalleryView.as_view(), name="gallery"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('partner/', views.PartnerView.as_view(), name="partner"),
    path('vacancie/', views.VacancieView.as_view(), name="vacancie"),
    path('usloviya/', views.UsloviyaView.as_view(), name="usloviya"),
    path('about/', views.AboutView.as_view(), name="about"),

    path('cources/<str:slug>/', views.CourcesDetailView.as_view(), name="category_detail"),

    path('teacher/', views.TeacherView.as_view(), name="teacher"),
    path('teacher/<slug:slug>/', views.TeacherDetailView.as_view(), name="teacher_detail"),

    path('news/', views.NewsView.as_view(), name="news"),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name="news_detail"),

    path('cluby-krujki/', views.ClubView.as_view(), name="club"),
    path('cluby-krujki/<slug:slug>/', views.ClubDetailView.as_view(), name="club_detail"),

    path('policy/', views.policy, name="policy"),
    path('politic-polojeniya/', views.politic_polojeniya, name="politic_polojeniya"),


]
