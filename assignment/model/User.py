from django.db import models
from django.contrib.auth.models import AbstractUser

from assignment.model.Accounts import Accounts
#These are the choices of the relationship for every user
relation_choices = (
    ("Father", "Father"),
    ("Child", "Child"),
    ("Mother", "Mother"),
    ("Grandfather", "Grandfather"),
    ("Grandmother", "Grandmother")
)


class User(AbstractUser):
    # additional fields that are required in the extended User model
    # phone number of the user
    number = models.CharField(max_length=15, null=True,blank=False)
    salary = models.FloatField(default=0)  # salary of the user
    # relation of the user in the family
    relation = models.CharField(
        max_length=20, choices=relation_choices, null=True)
    personal_expense = models.FloatField(default=0)
    # percentage this user will contribute to the family-fund, will be 0-1
    percentage = models.FloatField(default=0)
    account = models.ForeignKey(
        Accounts, on_delete=models.SET_NULL, null=True)  # Foreign Key linked to account

    def __str__(self):
        return self.username
