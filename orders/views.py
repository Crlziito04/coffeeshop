from django.views.generic import DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Orders,OrderProduct
from .forms import OrderProductForm
from django.urls import reverse_lazy
from rest_framework.views import(APIView)
from rest_framework.response import Response
from rest_framework import status
from .serializers import  OrdersSerializer

# Create your views here.
class MyOrderView(LoginRequiredMixin,DetailView):
  model =  Orders
  template_name ='orders/order.html'
  context_object_name ="order"

  def get_object(self):
    return Orders.objects.filter(isActive=True,user=self.request.user).first()
  
class CreateOrderProductView(LoginRequiredMixin,CreateView):
  template_name='orders/create_order_product.html'
  form_class = OrderProductForm
  success_url = reverse_lazy('order')

  def form_valid(self, form):
      order, _ = Orders.objects.get_or_create(
         isActive=True,
         user = self.request.user
      )
      form.instance.order = order
      form.instance.quantity = 1
      form.save()
      return super().form_valid( form)
  

class OrdersAPI(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self,request):
      orders = Orders.objects.all()
      serializer = OrdersSerializer(orders,many=True)
      return Response(serializer.data)

    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)