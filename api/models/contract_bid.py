from django.db import models

from django.utils.translation import gettext_lazy as _

from .contract import Contract
from .bid import Bid

# Cry about your models here
class ContractBid(models.Model):

    class Status(models.TextChoices):
      PLANNING = 'PL', _('Planning')
      PITCHING = 'PI', _('Pitching')
      SERVER = 'SV', _('Server')
      CLIENT = 'CL', _('Client')
      MVP = 'MV', _('MVP')
      STYLING = 'ST', _('Styling')
      COMPLETE = 'CM', _('Complete')

    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status.choices, default=None)

    def __str__(self):
        return (f"Contract:{self.contract_id}, bid won at: {self.bid_id}")