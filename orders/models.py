from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Orders(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  isActive = models.BooleanField(default=True)
  orderDate =models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"order {self.id} by {self.user}"
  
class OrderProduct(models.Model):
  order = models.ForeignKey(Orders, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  quantity = models.IntegerField()

  def __str__(self):
    return f"{self.order} - {self.product}"
  
  def get_order_products(self):
        return OrderProduct.objects.filter(order=self)