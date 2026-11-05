from django import forms


class GreetingForm(forms.Form):
    name = forms.CharField(
        label="Твоё имя",
        min_length=2,
        max_length=50,
        error_messages={
            "required": "Введите имя.",
            "min_length": "Имя должно содержать минимум 2 символа.",
            "max_length": "Имя должно содержать не больше 50 символов.",
        },
    )

    city = forms.CharField(
        label="Твой город",
        max_length=100,
        error_messages={
            "required": "Введите город.",
            "max_length": "Название города слишком длинное.",
        },
    )

    comment = forms.CharField(
        label="Ваш комментарий",
        max_length=1000,
        widget=forms.Textarea(attrs={"rows": 3}),
        error_messages={
            "max_length": "Комментарий должен содержать не больше 300 символов.",
        }
    )