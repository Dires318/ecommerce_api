from django.db import models
import uuid

class CommonsModel(models.Model):
    id = models.CharField(primary_key=True, unique=True,default=uuid.uuid4, editable=False, max_length=36)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField( auto_now=True)
    deleted_at = models.DateField()

    class Meta:
        abstract = "True"
    
    