from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('market_info/', MarketAPIList.as_view()),
    path('market_info/<int:pk>/', MarketAPIDetailView.as_view()),

    path('discount/', DiscountAPIList.as_view()),
    path('discount/<int:pk>/', DiscountAPIDetailView.as_view()),

    path('category/', CategoryAPIList.as_view()),
    path('category/<int:pk>/', CategoryAPIDetailView.as_view()),

    path('sub_category/', SubCategoryAPIList.as_view()),
    path('sub_category/<int:pk>/', SubCategoryAPIDetailView.as_view()),

    path('products/', ProductAPIList.as_view()),
    path('products/<int:pk>/', ProductAPIDetailView.as_view()),

    path('product_photo/', PhotoAPIList.as_view()),
    path('product_photo/<int:pk>/', PhotoAPIDetailView.as_view()),

    path('product_attribute/', ProductAttributeAPIList.as_view()),
    path('product_attribute/<int:pk>/', ProductAttributeAPIDetailView.as_view()),

    path('product_attribute_value/', ProductAttributeValueAPIList.as_view()),
    path('product_attribute_value/<int:pk>/', ProductAttributeValueAPIDetailView.as_view()),

    path('basket/', BasketAPIList.as_view()),
    path('basket/<int:pk>/', BasketAPIDetailView.as_view()),

    path('orders/', OrderAPIList.as_view()),
    path('orders/<int:pk>/', OrderAPIDetailView.as_view()),
]
