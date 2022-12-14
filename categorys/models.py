from django.db import models
from utils.model_utls import CommonsModel

# Create your models here.

class Category(CommonsModel):
    name = models.CharField(max_length=200)
    description = models.TextField()