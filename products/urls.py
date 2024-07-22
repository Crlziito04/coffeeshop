from django.urls import path
from .views import ProductFromView,GetProductsView,ProductListAPI

urlpatterns = [
    path('agregar/', ProductFromView.as_view(), name="add_product"),
    path("lista", GetProductsView.as_view(), name="get_products"),
    path("api/", ProductListAPI.as_view(), name="get_productsapi"),
] 
# if (settings.DEBUG):
#   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
