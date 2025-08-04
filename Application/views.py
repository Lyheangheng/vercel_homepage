

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
    user_number = 1  
    
    if request.method == "POST":
        if request.POST.get("number"):
            user_number = int(request.POST.get("number"))
    

    table_rows = []
    

    for multiplier in range(1, 11):  
        result = user_number * multiplier
        table_rows.append({
            'multiplier': multiplier,
            'user_number': user_number, 
            'result': result
        })
    
    context = {
        'message': 'Multiplication Table',
        'user_number': user_number,
        'table_rows': table_rows
    }
    return render(request, "multiplication_table.html", context)
from django.shortcuts import render