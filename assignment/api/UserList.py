from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializers import UserSerializer
from ..model import User
from rest_framework.permissions import IsAuthenticated


class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        data = UserSerializer(users, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Data not valid",status=status.HTTP_400_BAD_REQUEST)
