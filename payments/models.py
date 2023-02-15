from django.db import models
from utils.model_utls import CommonsModel
from orders.models import OrderDetail
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Discount(CommonsModel):
    name = models.CharField(_("discount name"), max_length=50)
    description = models.TextField(_("discount description"))
    discount_percent = models.DecimalField(_("discount percent"), max_digits=6, decimal_places=2)
    active = models.BooleanField(_("discount active"))

class PaymentDetail(CommonsModel):
    order = models.ForeignKey(OrderDetail, verbose_name=_("payment order"), on_delete=models.CASCADE)
    amount = models.IntegerField(_("payment amount"))
    provider = models.CharField(max_length = 150)
    status = models.CharField(_("payment status"), max_length=50)
    
    