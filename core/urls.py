from django.urls import path
from core.views import CustomTokenObtainPairView, ProtectedDataView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Custom login with email
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/me/', ProtectedDataView.as_view(), name='protected-data'),  # Protected API
]