from django.shortcuts import render, get_object_or_404
from web.models import Movie, Category


def index(request):
    product = Category.objects.all()[:3]
    movies = Movie.objects.filter(draf=False)
    return render(request, "web/index.html", {"movie_list": movies, "movie_cal": product})


def index1(request, url):
    tovar = Movie.objects.filter(category__url=url)
    return render(request, "web/tovar.html", {"movie_tovar": tovar})


def category(request):
    product = Category.objects.all()
    movies = Movie.objects.filter(draf=False)
    return render(request, "web/product.html", {"movie_call": product})


def contact(request):
    return render(request, "web/contact.html", {"contact_call": contact})


def delivery(request):
    return render(request, "web/delivery.html", {"delivery_call": delivery})


# def category2(request, url):
#     product = Category.objects.all()
#     tovary = Movie.objects.filter(category__url=url)
#     return render(request, "web/tovar.html", {"movie_tovary": tovary, "movie_call": product})






# # Create your views here.
