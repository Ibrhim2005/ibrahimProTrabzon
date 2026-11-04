from django.shortcuts import render


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
    name = request.GET.get("name", "").strip()
    number = request.GET.get("number", "").strip()
    context = {
        "title": "Приветствие",
        "name": name,
        "number": number,
    }

    return render(request, "core/greeting.html", context)