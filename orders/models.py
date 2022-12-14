from django.db import models
from utils.model_utls import CommonsModel

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class OrderDetail(CommonsModel):
    user = models.ForeignKey(User, verbose_name=_("order user"), on_delete=models.CASCADE)
    total = models.DecimalField(_("order total"), max_digits=15, decimal_places=2)
    

