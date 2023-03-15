from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F
from ..model import Accounts
from rest_framework.permissions import IsAuthenticated
from ..signals import month_changed
from ..serializers import AccountSerializer


class MonthList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        accounts = Accounts.objects.all()
        month_changed.send_robust(sender=accounts)
        data = AccountSerializer(accounts, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
