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
    name = ""
    error = ""
    city = ""
    success = False

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        city = request.POST.get("city", "").strip()

        if not name:
            error = "Введите имя."
        elif len(name) < 2:
            error = "Имя должно содержать минимум 2 символа."
        elif len(name) > 50:
            error = "Имя должно содержать не больше 50 символов."
        elif  not city:
            error = "Введите ваш город"
        else:
            success = True

    context = {
        "title": "POST-форма",
        "name": name,
        "city": city,
        "error": error,
        "success": success,
    }

    return render(request, "core/greeting.html", context)