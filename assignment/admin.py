from django.contrib import admin
from .model import Accounts, User, Billing, Expenses
# Register your models here.
admin.site.register(Accounts)
admin.site.register(User)
admin.site.register(Billing)
admin.site.register(Expenses)
