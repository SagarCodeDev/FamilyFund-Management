from django.db import models
from django.contrib.auth.models import AbstractUser
from .model import Accounts,User,Expenses,Billing
# relation_choices=(
#         ("Father","Father"),
#         ("Child","Child"),
#         ("Mother","Mother"),
#         ("Grandfather","Grandfather"),
#         ("Grandmother","Grandmother")
#     )

# class Accounts(models.Model):
#     #all the fields required in Accounts model
#     family_fundname=models.CharField(max_length=20,default="Fund Name")
#     family_fund=models.IntegerField()
#     goal_amount=models.IntegerField()
#     saved_money=models.IntegerField()
#     def __str__(self):
#         return self.family_fundname
# class User(AbstractUser):
#     #additional fields that are required in the extended User model
#     number=models.CharField(max_length=15,null=True)   #phone number of the user
#     salary=models.IntegerField(default=0)    #salary of the user
#     relation=models.CharField(max_length=20,choices=relation_choices,null=True)  #relation of the user in the family
#     personal_expense=models.IntegerField(default=0)
#     percentage=models.IntegerField(null=True) #percentage this user will contribute to the family-fund
#     account=models.ForeignKey(Accounts,on_delete=models.CASCADE,null=True) #Foreign Key
#     def __str__(self):
#         return self.username
# class Expenses(models.Model):
#     #all the fields in the Expenses model
#     amount=models.IntegerField()
#     date=models.DateField()
#     account=models.ForeignKey(User,on_delete=models.CASCADE)
# class Billing(models.Model):
#     #all the fields in the Billing model
#     item_name=models.CharField(max_length=30)
#     quantity=models.IntegerField()
#     expense=models.OneToOneField(Expenses,on_delete=models.CASCADE)