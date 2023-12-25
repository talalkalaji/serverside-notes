from django.db import models
from table.models import Table

class Bill (models.Model):
    table = models.ForeignKey(Table,on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    leaving_time = models.DateTimeField()
    sits = models.IntegerField()
    time_cost = models.DecimalField(decimal_places=2,max_digits=8)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2,max_digits=8)
    
    class Meta:
        db_table = "Bill"
        ordering = ["table","entry_time"]
        