
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us', views.about_us, name="about-us"),
    path('apps', views.apps, name="apps"),
    path('contact', views.contact, name="contact"),
    path('news', views.news, name="news"),
    path('article-website', views.article_website, name="article-website"),
    path('article-customer', views.article_customer, name="article-customer"),
    path('article-covid-19', views.article_covid_19, name="article-covid-19"),


]
