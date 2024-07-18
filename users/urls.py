from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDeleteAPIView, UserListAPIView,
                         UserRetrieveAPIView, UserTokenObtainPairView,
                         UserUpdateAPIView)

app_name = UsersConfig.name


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListAPIView.as_view(), name="list"),
    path("retrieve/<int:pk>/", UserRetrieveAPIView.as_view(), name="retrieve"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete"),
    path("login/", UserTokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
