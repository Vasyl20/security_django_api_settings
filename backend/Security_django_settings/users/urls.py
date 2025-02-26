from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import user_list

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # отримання access і refresh токенів
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # оновлення токену
    path('users/', user_list, name='user_list'),  # ендпоінт для отримання списку користувачів
]
