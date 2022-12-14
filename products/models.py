from django.db import models
from utils.model_utls import CommonsModel
from categorys.models import Category
from payments.models import Discount
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class ProductInventory(CommonsModel):
    quantity = models.IntegerField(_("quantity"))



class Product(CommonsModel):
    name = models.CharField(max_length=200)
    description = models.TextField(_("description"))
    sku = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    price = models.DecimalField(_("product price"), max_digits=15, decimal_places=2)
    discount = models.ForeignKey(Discount, verbose_name=_(""), on_delete=models.CASCADE)
    

    
    


