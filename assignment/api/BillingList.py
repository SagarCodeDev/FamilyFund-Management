from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers import BillingSerializer
from ..model import Billing, Expenses
from rest_framework.permissions import IsAuthenticated


class BillingList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        billing = Billing.objects.all()
        if billing:
            data = BillingSerializer(billing, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        return Response("No Bills available", status=status.HTTP_200_OK)

    def post(self, request, format=None):
        expense = get_object_or_404(Expenses, pk=request.data["expense"])
        serializer = BillingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            billing = serializer.save()
            expense.billing = billing
            expense.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)
