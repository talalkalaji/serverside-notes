from django.db import models
from supplier.models import Supplier

class BillSupplier(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=12)
    paid = models.DecimalField(decimal_places=2, max_digits=12, blank=True)
    due = models.DecimalField(decimal_places=2, max_digits=12, blank=False, editable=False)
    date = models.DateField()
    details = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.due = self.total - self.paid
        super(BillSupplier, self).save(*args, **kwargs)
    @property
    def remaining(self):
        return round(self.due, 2)
    class Meta:
        db_table= "BillSupplier"
