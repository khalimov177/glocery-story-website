from django.urls import path ,include
from .views import *

urlpatterns = [
    path('',product_list, name='product_list'),
    path('users/', include('users.urls')),
    path('delete_cart_item/<int:pk>',delete_cart_item, name='delete_cart_item'),
    path('create_order', create_order, name='create_order'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('rate_product/<int:pk>', rate_product, name='rate_product'),
]