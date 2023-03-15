from django.db import models


class Accounts(models.Model):
    # all the fields required in Accounts model
    family_fundname = models.CharField(max_length=20, default="Fund Name")
    family_fund = models.FloatField(default=0)
    goal_amount = models.FloatField()
    saved_money = models.FloatField(default=0)

    def __str__(self):
        return self.family_fundname
