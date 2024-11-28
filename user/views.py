from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data
            refresh = RefreshToken.for_user(serializer.instance)
            res = {
                "user": user,
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

