from django.db import models

# Create your models here.

class Conversion(models.Model):
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    converted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

