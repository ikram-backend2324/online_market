from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Market Info


class OnlineMarket(models.Model):
    market_name = models.CharField(max_length=150)
    market_phone_number = models.IntegerField()
    market_description = models.TextField()

    def __str__(self):
        return self.market_name

    class Meta:
        verbose_name = 'Online Market'
        verbose_name_plural = 'Online Market'


# Product Category


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='s_category', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

# Products


class Products(models.Model):
    product_name = models.CharField(max_length=150)
    product_price = models.IntegerField()
    product_description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, related_name='products_sub_category', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.product_name

# Product Discount


class Discount(models.Model):
    discount = models.CharField(max_length=150)
    term = models.DateTimeField()
    products = models.ManyToManyField(Products)

    def __str__(self):
        return self.discount

# Photos For Product


class Photos(models.Model):
    """Photos For Product"""
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    product = models.ForeignKey(Products, related_name='photos_product', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.photo)

# Product Attribute


class ProductAttribute(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

# Value For Product Attribute


class ProductAttributeValue(models.Model):
    product = models.ManyToManyField(Products, blank=True)
    product_attribute = models.ManyToManyField(ProductAttribute, related_name='product_attribute', blank=True)
    value = models.CharField(max_length=150)

    def __str__(self):
        return str(self.value)

# Basket For Products


class Basket(models.Model):
    product = models.ManyToManyField(Products)

# Orders


class Orders(models.Model):
    CHOICES = (
        ("Online card", "using an online card"),
        ("Cash/Card upon receipt", "in cash or By card upon receipt"),
    )
    basket = models.ManyToManyField(Basket)
    user = models.ManyToManyField(User)
    delivery_address = models.CharField(max_length=150)
    payment_method = models.CharField(max_length=150, choices=CHOICES)



