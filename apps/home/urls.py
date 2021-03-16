from django.urls import path
from apps.home import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('news/', views.NewsView.as_view(), name="news"),
    path('gallery/', views.GalleryView.as_view(), name="gallery"),
    path('teacher/', views.TeacherView.as_view(), name="teacher"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('partner/', views.PartnerView.as_view(), name="partner"),
    path('vacancie/', views.VacancieView.as_view(), name="vacancie"),
    path('usloviya/', views.UsloviyaView.as_view(), name="usloviya"),
    path('about/', views.AboutView.as_view(), name="about"),

]
