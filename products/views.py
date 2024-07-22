from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from django.views.generic import TemplateView
from .models import Product

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