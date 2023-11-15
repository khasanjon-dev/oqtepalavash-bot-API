from django.db.models import CharField, Model, TextField


class About(Model):
    text = TextField()

    def __str__(self):
        return self.text


class Menu(Model):
    text = TextField()
    link = CharField(max_length=250)

    def __str__(self):
        return self.text
