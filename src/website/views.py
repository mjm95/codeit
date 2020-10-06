from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home.html", {})


def about_us(request):
    return render(request, "about-us.html", {})


def apps(request):
    return render(request, "apps.html", {})


def contact(request):
    return render(request, "contact.html", {})


def news(request):
    return render(request, "news.html", {})


def article_covid_19(request):
    return render(request, "article-covid-19.html", {})


def article_customer(request):
    return render(request, "article-customer.html", {})


def article_website(request):
    return render(request, "article-website.html", {})
