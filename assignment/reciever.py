from django.dispatch import receiver
from .signals import *
from django.db.models import Sum
from django.db.models import F


@receiver(account_created)
def connect_users(sender, users, **kwargs):
    #to use to connect the user
    for user in users:
        sender.user_set.add(user) 
    #updating the values of the family-fund and saved money after addition of every user 
    sender.family_fund = sender.user_set.filter(is_active=True).aggregate(
        salary_sum=Sum(F('salary') * F('percentage')))['salary_sum']
    sender.saved_money = sender.user_set.aggregate(salary_sum=Sum(
        F('salary') * (1 - F('percentage'))))['salary_sum']
    sender.save()


@receiver(month_changed)
def update_account(sender, **kwargs):
    #to update the values at the end of the month
    for account in sender:
        sum_salary = account.user_set.filter(is_active=True).aggregate(salary_sum=Sum(
            F('salary') * F('percentage')))['salary_sum']/100
        saved_expense = account.user_set.aggregate(salary_sum=Sum(
            F('salary') * (100 - F('percentage'))))['salary_sum']
        account.saved_money += account.family_fund+saved_expense
        account.family_fund = sum_salary
        account.save()
