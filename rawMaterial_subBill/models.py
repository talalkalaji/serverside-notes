from django.db import models
from rawmaterials.models import RawMaterial
from sup_bill.models import BillSupplier

class RawMaterialSupplierBill(models.Model):
    supplier = models.ForeignKey(BillSupplier, on_delete=models.CASCADE, null=False)
    rawMaterial = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, null=False)
    date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True)
    quantity = models.IntegerField(null=False)
    rawPrice = models.DecimalField(decimal_places=2, max_digits=12, null=False)
    quantityPrice = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    class Meta:
        db_table = "RawMaterialSupplierBill"

    def save(self, *args, **kwargs):
        self.quantityPrice = self.quantity * self.rawPrice
        rawMaterial = self.rawMaterial
        rawMaterial.quantity += self.quantity
        rawMaterial.save()

        super(RawMaterialSupplierBill, self).save(*args, **kwargs)
