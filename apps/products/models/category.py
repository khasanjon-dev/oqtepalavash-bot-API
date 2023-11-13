from django.db.models import Model, CharField


class Category(Model):
    name = CharField(max_length=150)

    def __str__(self):
        return self.name
