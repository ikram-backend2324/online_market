from django.shortcuts import render
from .models import *
# from django_filters import rest_framework as filters
from rest_framework import filters
from rest_framework import generics, viewsets, status
from rest_framework.permissions import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.
# Market Info


class MarketAPIList(generics.ListCreateAPIView):
    queryset = OnlineMarket.objects.all()
    serializer_class = OnlineMarketSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class MarketAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OnlineMarket.objects.all()
    serializer_class = OnlineMarketSerializer

# Discount


class DiscountAPIList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

# Category


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Sub Category


class SubCategoryAPIList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


# Product


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'product_price']


class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

# Photos for Product


class PhotoAPIList(generics.ListCreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer


class PhotoAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

# Product attribute


class ProductAttributeAPIList(generics.ListCreateAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class ProductAttributeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer

# Product Attribute Value


class ProductAttributeValueAPIList(generics.ListCreateAPIView):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer


class ProductAttributeValueAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer

# Product Basket


class BasketAPIList(generics.ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


# Orders

class OrderAPIList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


