from django.db import models

class Account(models.Model):
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)

class EventType(models.Model):
    name = models.CharField(max_length=100)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_time = models.DateTimeField()
    txn_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
