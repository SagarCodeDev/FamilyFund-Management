from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import F
from ..serializers import AccountSerializer, UserSerializer
from ..model import Accounts
from rest_framework.permissions import IsAuthenticated
from ..signals import account_created


class AccountList(APIView):
    permission_classes = (IsAuthenticated,)

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
            #used signals here to notify of the account creatiion and linking all the associated users to the account
            account_created.send_robust(sender=account, users=iterate)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)
