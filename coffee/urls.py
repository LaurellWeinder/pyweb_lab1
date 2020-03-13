from django.contrib import admin
from django.urls import path
from coffee.views import *

urlpatterns = [
    path('', DefaultPage.as_view()),
    path('about/', AboutPage.as_view()),
    path('blog/', BlogPage.as_view()),
    path('blog-single/', BlogSinglePage.as_view()),
    path('cart/', CartPage.as_view()),
    path('checkout/', CheckoutPage.as_view()),
    path('contact/', ContactPage.as_view()),
    path('menu/', MenuPage.as_view()),
    path('product-single/', ProductPage.as_view()),
    path('services/', ServicesPage.as_view()),
    path('shop/', ShopPage.as_view()),
]
