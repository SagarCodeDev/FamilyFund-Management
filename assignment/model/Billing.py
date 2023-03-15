from django.db import models
from assignment.model.Expense import Expenses


class Billing(models.Model):
    # all the fields in the Billing model
    item_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    expense = models.OneToOneField(Expenses, on_delete=models.CASCADE)
