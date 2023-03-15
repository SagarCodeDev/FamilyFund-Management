from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers import BillingSerializer
from ..model import Billing
from rest_framework.permissions import IsAuthenticated


class BillingDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        billing = get_object_or_404(Billing, pk=pk)
        data = BillingSerializer(billing).data
        return Response(data)

    def patch(self, request, pk):
        billing = get_object_or_404(Billing, pk=pk)
        serializer = BillingSerializer(
            billing, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_206_PARTIAL_CONTENT)
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        billing = get_object_or_404(Billing, pk=pk)
        billing.delete()
        return Response("Bill successfuly deleted",status=status.HTTP_204_NO_CONTENT)
