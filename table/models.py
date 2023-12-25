from django.core.exceptions import ValidationError
from django.db import models

class Table(models.Model):      
    def validate_table_number(value):
        if value >= 9:
            raise ValidationError('Table number must be less than 9.')
  
    table_number = models.IntegerField(unique=True, validators=[validate_table_number])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['table_number']
        db_table = "Table"
        
