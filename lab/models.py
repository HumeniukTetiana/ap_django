import re
from django.db import models
from .repositories import BaseRepository

# class Person(models.Model):
#     first_name = models.CharField('імя', max_length=50)
#     last_name = models.CharField('прізвище', max_length=50)
#     phone = models.CharField('телефон', max_length=15, null=True, blank=True)
#     email = models.EmailField('емеіл', max_length=100)
#
#     @staticmethod
#     def is_valid_email(email: str) -> bool:
#         return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
#
#     @staticmethod
#     def is_valid_phone(phone: str) -> bool:
#         return bool(re.match(r"^\+?\d{10,15}$", phone))
#
#     #Метод що буде перевизначатись
#     def show_info(self):
#         pass
#
#     def __str__(self):
#         return self.first_name
#
#     class Meta:
#         verbose_name = 'людина'
#         verbose_name_plural = 'люди'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


# class FullOrder(models.Model):
#     PAYMENT_STATUS = [
#         ('yes', 'Yes'),
#         ('no', 'No'),
#     ]
#
#     person = models.ForeignKey(Person, blank=True, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now = True)
#     payment = models.CharField(max_length=3, choices=PAYMENT_STATUS)
#     total_amount = models.DecimalField(max_digits=8, decimal_places=1)
#     points_used = models.IntegerField(null=True, blank=True)
#
#     def __str__(self):
#         return f"Order {self.pk}"
#
#
# class Product(models.Model):
#     product_name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     product_description = models.TextField()
#     category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.product_name
#
#
# class OrderDetails(models.Model):
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     full_order = models.ForeignKey(FullOrder, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Order detail {self.pk}"
#
