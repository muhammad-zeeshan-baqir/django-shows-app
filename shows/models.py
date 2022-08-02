from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to="upload/")

    def __str__(self):
        return self.name


class Dresses(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to="upload/")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dresses = models.ForeignKey(Dresses, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="upload/")
    price = models.IntegerField()
    discount = models.IntegerField()

    @property
    def discount_price(self):
        discounts = self.price * self.discount / 100
        return self.price - discounts


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()
