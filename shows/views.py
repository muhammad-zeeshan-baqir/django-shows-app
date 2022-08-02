from django.shortcuts import render
from .models import Category


def index(request):
    category = Category.objects.all()
    context = {"category": category}
    return render(request, "index.html", context)


def checkout(request):
    return render(request, "checkout.html")


def cart(request):
    return render(request, "cart.html")


def contact(request):
    return render(request, "contact.html")


def detail(request):
    return render(request, "detail.html")


def shop(request):
    return render(request, "shop.html")


def form(request):
    return render(request, "form.html")
