from django.db import models


class RawMaterial(models.Model):
    name = models.CharField(unique=True, max_length=254, null=False, blank=False)
    details = models.CharField(unique=True, max_length=254, null=False, blank=False)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    image = models.ImageField(upload_to="RawMaterials/")
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    quantity_price = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.quantity_price = self.quantity * self.price
        super(RawMaterial, self).save(*args, **kwargs)

    class Meta:
        db_table = "RawMaterial"
