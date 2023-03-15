from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers import ExpenseSerializer
from ..model import Expenses
from rest_framework.permissions import IsAuthenticated


class ExpensesDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        expense = get_object_or_404(Expenses, pk=pk)
        data = ExpenseSerializer(expense).data
        return Response(data)

    def patch(self, request, pk):
        expense = get_object_or_404(Expenses, pk=pk)
        serializer = ExpenseSerializer(
            expense, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_206_PARTIAL_CONTENT)
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = get_object_or_404(Expenses, pk=pk)
        expense.delete()
        return Response("Data not valid",status=status.HTTP_204_NO_CONTENT)
