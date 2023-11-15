from django.db.models import CharField, DateTimeField, IntegerField, Model


class User(Model):
    first_name = CharField(max_length=250, null=True, blank=True)
    last_name = CharField(max_length=250, null=True, blank=True)
    username = CharField(max_length=100, null=True, blank=True)
    telegram_id = IntegerField(unique=True)
    phone = CharField(max_length=15, unique=True)
    city = CharField(max_length=100)
    # date
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True, null=True)
