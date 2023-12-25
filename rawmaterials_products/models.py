from django.db import models
from products.models import Product
from rawmaterials.models import RawMaterial

class RawMaterialProduct(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rawmaterial_quantity = models.IntegerField()
    class Meta:
        db_table = "RawMaterialProduct"
        unique_together = ('product', 'raw_material',)
