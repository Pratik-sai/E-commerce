from django.urls import path
from .views import OrderView, CartView

urlpatterns=[
    path('orders',OrderView.as_view()),
    path('carts',CartView.as_view()),
]