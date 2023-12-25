from django.db import models

class Category (models.Model):
    name = models.CharField(max_length= 50 , null=False, unique= True
)
    image = models.ImageField(upload_to="categories/")
    note = models.TextField(null=True)
    
    class Meta:
        db_table = "category"