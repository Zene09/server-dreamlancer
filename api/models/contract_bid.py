from django.db import models

from .contract import Contract
from .bid import Bid

# Cry about your models here
class ContractBid(models.Model):
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE)
    can_bid = models.BooleanField(default=False)

    def __str__(self):
        return (f"Contract:{self.contract_id}, bid won at: {self.bid_id}")