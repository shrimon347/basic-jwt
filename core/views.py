from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProtectedDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "message": "This is a protected API endpoint!",
            "user": str(request.user.username),
            "email": request.user.email,
            "contactNumber": request.user.contact_number,
        }
        return Response(data)
