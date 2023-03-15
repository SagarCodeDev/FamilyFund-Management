from django.urls import path
from assignment.api.AccountDetail import AccountDetail
from assignment.api.AccountList import AccountList
from assignment.api.BillingDetail import BillingDetail
from assignment.api.BillingList import BillingList
from assignment.api.ExpensesDetail import ExpensesDetail
from assignment.api.ExpensesList import ExpensesList
from assignment.api.GoalAmountList import GoalAmountList
from assignment.api.MonthList import MonthList
from assignment.api.PersonalSpendList import PeronalSpendList
from assignment.api.UserDetail import UserDetail
from assignment.api.UserList import UserList
urlpatterns = [

    path('api/accounts/', AccountList.as_view(), name='all-account'),
    path('api/accounts/<int:pk>/', AccountDetail.as_view(), name='account'),
    path('api/expense/',
         ExpensesList.as_view(), name='all-expense'),
    path('api/expense/<int:pk>',
         ExpensesDetail.as_view(), name='expense'),
    path('api/billing/',
         BillingList.as_view(), name='all-billing'),
    path('api/billing/<int:pk>',
         BillingDetail.as_view(), name='billing'),
    path('api/users/', UserList.as_view(), name='all-user'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user'),
    path('api/monthchange/', MonthList.as_view(), name='month-change'),
    path('api/users/expense/<int:pk>/',
         PeronalSpendList.as_view(), name='expense'),
    path('api/accounts/goalamount/<int:pk>/',
         GoalAmountList.as_view(), name='goal-amount')
]
