from django.db.models import CASCADE, ForeignKey, IntegerField, Model
from products.models import Product
from users.models import User


class Favorite(Model):
    # relationships
    user = ForeignKey(User, CASCADE, 'favorites')
    product = ForeignKey(Product, CASCADE, 'favorites')

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return self.product.name + ' ' + self.user.phone


class Basket(Model):
    quantity = IntegerField(default=1)
    # relationships
    user = ForeignKey(User, CASCADE, 'basket')
    product = ForeignKey(Product, CASCADE, 'basket')

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return self.product.name + ' ' + self.user.phone
