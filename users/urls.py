from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, UserProfileAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='registration'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('update_profile/<int:pk>/', UserUpdateAPIView.as_view(), name='profile_update'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
