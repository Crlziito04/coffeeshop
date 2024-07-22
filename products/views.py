from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .serializers import ProductSerializer
from .models import Product
from rest_framework.views import(APIView)
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductFromView(generic.FormView):
  template_name = 'products/add_product.html'

  form_class = ProductForm
  success_url = reverse_lazy('get_products')

  def form_valid(self, form):
      form.save()
      return super().form_valid(form)

class GetProductsView(generic.ListView):
  #  template_name = "products/get_products.html"

  #  def get_context_data (self):
  #     products_list = Product.objects.all()
  #     return {
  #     "products_list": products_list
  #   }
  model = Product
  template_name = 'products/get_products.html'
  context_object_name = 'products'

class ProductListAPI(APIView):
   authentication_classes=[]
   permission_classes=[]

   def get(self,request):
      products = Product.objects.all()
      serializer = ProductSerializer(products,many=True)
      return Response(serializer.data)
   
   def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)