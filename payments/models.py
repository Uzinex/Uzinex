from django.db import models
from marketplace.models import Contract


class Transaction(models.Model):
    STATUS_CHOICES = [
        ("held", "held"),
        ("released", "released"),
    ]
    contract = models.OneToOneField(Contract, related_name="transaction", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="held")
    provider = models.CharField(max_length=50, default="stub")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Transaction for {self.contract_id}"
