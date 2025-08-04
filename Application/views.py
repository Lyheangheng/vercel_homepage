from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def home(request):
    return render(request, "index.html")


def forPage(request):
    context = {}
    context["count"] = list(range(0, 10))
    return render(request, "for.html", context)
