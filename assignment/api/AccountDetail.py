from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers import AccountSerializer
from ..model import Accounts
from rest_framework.permissions import IsAuthenticated


class AccountDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        data = AccountSerializer(account).data
        return Response(data)

    def delete(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        account.delete()
        return Response("Account sucessfully deleted",status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        account = get_object_or_404(Accounts, pk=pk)
        serializer = AccountSerializer(
            account, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_206_PARTIAL_CONTENT)
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)
