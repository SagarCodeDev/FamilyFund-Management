from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers import UserSerializer
from ..model import User
from rest_framework.permissions import IsAuthenticated


class UserDetail(APIView):
    permission_classes = (IsAuthenticated,)

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
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.is_active=False
        user.save()
        return Response("User succesfuly deleted", status=status.HTTP_204_NO_CONTENT)
