"""from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F
from django.shortcuts import get_object_or_404
from ..serializers import AccountSerializer, UserSerializer, ExpenseSerializer, BillingSerializer
from ..models import Accounts, User, Expenses, Billing


class AccountList(APIView):
    def get(self, request):
        accounts = Accounts.objects.all()
        data = AccountSerializer(accounts, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data["Account"])
        if serializer.is_valid(raise_exception=True):
            example = UserSerializer(data=request.data["User"], many=True)
            if example.is_valid(raise_exception=True):
                iterate = example.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            account = serializer.save()
            for user in iterate:
                account.user_set.add(user)#use signals
            account.family_fund = account.user_set.aggregate(
                salary_sum=Sum(F('salary') * F('percentage')))['salary_sum']/100
            account.saved_money = account.user_set.aggregate(salary_sum=Sum(
                F('salary') * (100 - F('percentage'))))['salary_sum']/100
            account.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(APIView):
    def get(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        data = AccountSerializer(account).data
        return Response(data)

    def delete(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        serializer = AccountSerializer(
            account, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response("Account Successfuly Deleted", status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        data = UserSerializer(users, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request, pk):
        users = get_object_or_404(User, pk=pk)
        data = UserSerializer(users).data
        return Response(data)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response("User succesfuly deleted", status=status.HTTP_204_NO_CONTENT)


class ExpensesList(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        expense = user.expenses_set.all()
        data = ExpenseSerializer(expense, many=True).data
        return Response(data)

    def post(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = ExpenseSerializer(data=request.data["expense"])
        amount = request.data["expense"]["amount"]
        expense_type = request.data["type"]
        if serializer.is_valid(raise_exception=True):
            if expense_type == "family":
                if user.account.family_fund > amount:
                    user.account.family_fund -= amount
                    expense = serializer.save()
                    user.expenses_set.add(expense)
                    user.save()
                    user.account.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response("Family fund exhausted", status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                x = user.personal_expense-amount
                user.personal_expense -= amount
                user.account.family_fund -= amount
                user.save()
                if x > 0:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response("Personal expense exhausted", status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ExpensesDetail(APIView):
    def get(self, request, pk, pk1):
        expense = get_object_or_404(Expenses, pk=pk)
        data = ExpenseSerializer(expense).data
        return Response(data)

    def patch(self, request, pk, pk1):
        expense = get_object_or_404(Expenses, pk=pk)
        serializer = ExpenseSerializer(
            expense, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, pk1):
        expense = get_object_or_404(Expenses, pk=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BillingList(APIView):
    def get(self, request, pk):
        expense = get_object_or_404(Expenses, pk=pk)
        if (hasattr(expense, 'billing')):
            billing = expense.billing
            data = BillingSerializer(billing, many=True).data
            return Response(data)
        return Response("Bill not Generated", status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        expense = get_object_or_404(Expenses, pk=pk)
        serializer = BillingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            billing = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BillingDetail(APIView):
    def get(self, request, pk, pk1):
        billing = get_object_or_404(Billing, pk=pk)
        data = BillingSerializer(billing).data
        return Response(data)

    def patch(self, request, pk, pk1):
        billing = get_object_or_404(Billing, pk=pk)
        serializer = BillingSerializer(
            billing, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, pk1):
        billing = get_object_or_404(Billing, pk=pk)
        billing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MonthList(APIView):
    def get(self, request):
        accounts = Accounts.objects.all()
        for account in accounts:
            sum_salary = account.user_set.aggregate(salary_sum=Sum(
                F('salary') * F('percentage')))['salary_sum']/100
            saved_expense = account.user_set.aggregate(salary_sum=Sum(
                F('salary') * (100 - F('percentage'))))['salary_sum']
            account.saved_money += account.family_fund+saved_expense
            account.family_fund = sum_salary
            account.save()
        return Response(status=status.HTTP_200_OK)


class PeronalSpendList(APIView):
    def get(self, request, pk):
        spend = get_object_or_404(User, pk=pk).personal_expense
        if spend <= 0:
            return Response("Personal Expense Exhausted", status=status.HTTP_200_OK)
        return Response({"spend": spend}, status=status.HTTP_202_ACCEPTED)


class GoalAmountList(APIView):
    def get(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        current = account.goal_amount-account.saved_money
        if current > 0:
            return Response({"Amount Needed": current}, status=status.HTTP_200_OK)
        return Response({"Amount Needed": "Goal Reached"}, status=status.HTTP_200_OK)
"""