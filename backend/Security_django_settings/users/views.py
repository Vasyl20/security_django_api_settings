from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Перевіряється, чи користувач аутентифікований
def user_list(request):
    users = User.objects.all()
    user_data = [{"id": user.id, "username": user.username} for user in users]
    return Response(user_data)
