from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path('service_details/<slug>/',views.service_detail,name='service_detail'),
    path("blog/", views.blog, name="blog"),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path("contact/", views.contact, name="contact"),
    path('pricing/',views.pricing,name='pricing'),
    path('team/<slug:slug>/', views.team_detail, name='team_detail'),
    path("enquery/", views.enquery, name="enquery"),
]