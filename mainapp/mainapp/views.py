from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    user = request.user
    products = [""]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)