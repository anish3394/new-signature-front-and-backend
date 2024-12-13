from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .models import User
from .signature import *
from .serializers import UserSerializer
from .serializers import UserListSerializer


class UserListView(APIView):
    # permission_classes = [IsAdminUser]  # Only admin users can access this view

    def get(self, request):
        users = User.objects.all()  # Get all user accounts
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
class SignupView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(email=email)

        if created:
            return Response({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user:
            return Response({'success': True, 'message': 'Login successful', 'sig':sig2}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email'}, status=status.HTTP_404_NOT_FOUND)
