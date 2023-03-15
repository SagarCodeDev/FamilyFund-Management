from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..model import Accounts
from rest_framework.permissions import IsAuthenticated


class GoalAmountList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        current = account.goal_amount-account.saved_money
        if current > 0:
            return Response({"Amount Needed": current}, status=status.HTTP_200_OK)
        return Response({"Amount Needed": "Goal Reached"}, status=status.HTTP_200_OK)
