from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..model import User
from rest_framework.permissions import IsAuthenticated


class PeronalSpendList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        spend = get_object_or_404(User, pk=pk).personal_expense
        if spend <= 0:
            return Response("Personal Expense Exhausted", status=status.HTTP_200_OK)
        return Response({"spend": spend}, status=status.HTTP_202_ACCEPTED)
