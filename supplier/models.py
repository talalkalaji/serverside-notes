from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    
    class Meta :
        db_table = "Supplier"
