from django.db.models import CharField, DateTimeField, IntegerField, Model, TextChoices


class User(Model):
    class Language(TextChoices):
        UZ = 'uz', 'uzbek'
        RU = 'ru', 'russian'
        EN = 'en', 'english'

    telegram_id = IntegerField(unique=True)
    phone = CharField(max_length=15, unique=True, null=True, blank=True)
    city = CharField(max_length=100, null=True, blank=True)
    # choices
    language = CharField(max_length=2, choices=Language.choices, null=True, blank=True)
    # date
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True, null=True)
