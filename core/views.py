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
