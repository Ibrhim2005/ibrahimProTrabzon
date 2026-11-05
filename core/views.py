from django.shortcuts import render

from .forms import GreetingForm


def home(request):
    context = {
        "title": "Моё обучение",
        "name": "Али",
        "learning_started": True,
        "completed_lessons": 2,
        "courses": [
            {"name": "Python", "lessons": 20},
            {"name": "Django", "lessons": 30},
            {"name": "JavaScript", "lessons": 15},
        ],
    }
    return render(request, "core/home.html", context)

def about(request):
    context = {
        "title": "О сайте",
        "description": "Это мой учебный сайт на Django.",
    }



    return render(request, "core/about.html", context)

def greeting(request):
    result = ""

    if request.method == "POST":
        form = GreetingForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            city = form.cleaned_data["city"]

            result = f"Привет, {name}! Твой город: {city}."
    else:
        form = GreetingForm()

    context = {
        "title": "Django Forms",
        "form": form,
        "result": result,
    }

    return render(request, "core/greeting.html", context)