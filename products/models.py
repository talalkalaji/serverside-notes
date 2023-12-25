from django.db import models
from categories.models import Category


class Product (models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200 ,null=False)
    price = models.DecimalField(decimal_places=2, max_digits=9 ,null=False)
    details = models.CharField(max_length=240, null=True)
    image = models.ImageField(null=False ,blank = True,upload_to="products/" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table ="Product"
