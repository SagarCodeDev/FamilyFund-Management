import datetime
from django.db import models
from assignment.model.User import User
from django.utils.timezone import now

class Expenses(models.Model):
    # all the fields in the Expenses model
    amount = models.FloatField()
    date = models.DateField(default=now)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
