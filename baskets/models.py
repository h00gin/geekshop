from django.db import models
from django.utils.functional import cached_property

from users.models import User
from products.models import Product


# class BasketQuerySet(models.QuerySet):
#
#     def delete(self):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#         super().delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum_1(self):
        return self.quantity * self.product.price

    product_cost = property(sum_1)

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    def total_quantity(self):
        _items = self.get_items_cached
        return sum(list(map(lambda x: x.quantity, _items)))

    def total_sum(self):
        _items = self.get_items_cached
        return sum(list(map(lambda x: x.product_cost, _items)))


    #
    # def total_quantity(self):
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum(basket.quantity for basket in baskets)
    #
    # def total_sum(self):
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum(basket.sum() for basket in baskets)
    #

    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete()


