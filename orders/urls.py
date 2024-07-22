from django.urls import path
from .views import MyOrderView, CreateOrderProductView, OrdersAPI

urlpatterns = [
    path('mi-orden',MyOrderView.as_view(), name="order"),
    path('agregarProducto',CreateOrderProductView.as_view(),name='addProduct'),
    path("api/",OrdersAPI.as_view(), name="order_api"),
]
