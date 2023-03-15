from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers import ExpenseSerializer
from ..model import User, Expenses
from rest_framework.permissions import IsAuthenticated


class ExpensesList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        expense = Expenses.objects.all()
        if expense:
            data = ExpenseSerializer(expense, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        return Response("No expense generated", stats=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = get_object_or_404(User, pk=request.data["expense"]["account"])
        if (user.is_active == False):
            return Response("Not an active user", status=status.HTTP_400_BAD_REQUEST)
        if (not user.account):
            return Response("This user is not linked to any account", status=status.HTTP_400_BAD_REQUEST)
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
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)
