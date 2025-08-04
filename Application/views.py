

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

    context["message"] = "Django loop"

    if request.method == "POST" and request.POST["count"] != "":
        number = int(request.POST.get("count"))
        context["count"] = list(range(1, number + 1))
    else:
        context["count"] = list(range(1, 2))

    return render(request, "for.html", context)

def multiplication_table(request):
    context = {}
    context["message"] = "Django Multiplication Table"

    if request.method == "POST" and request.POST.get("number"):
        number = int(request.POST.get("number"))
    else:
        number = 1

    table = [(i, number * i) for i in range(1, number + 1)]
    context["number"] = number
    context["table"] = table

    return render(request, "multiplication_table.html", context)
from django.shortcuts import render