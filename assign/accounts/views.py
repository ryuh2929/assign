from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import User

class AccountListAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            pass
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def post(self, request):

        request_data = request.data

        serializer = UserSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)