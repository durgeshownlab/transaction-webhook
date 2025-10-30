from django.db import models

# Create your models here.
class Transaction(models.Model):
  transaction_id = models.CharField(max_length=64, unique=True, db_index=True)
  source_account = models.CharField(max_length=64)
  destination_account = models.CharField(max_length=64)
  amount = models.DecimalField(max_digits=12, decimal_places=2)
  currency = models.CharField(max_length=3)
  STATUS_CHOICES = [
    ("PROCESSING", "PROCESSING"),
    ("PROCESSED", "PROCESSED"),
  ]
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PROCESSING")
  created_at = models.DateTimeField(auto_now_add=True)
  processed_at = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return self.transaction_id