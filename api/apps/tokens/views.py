from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.tokens.serializers import TokenCreateSerializer
from apps.tokens.service import TokenService


class TokenCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TokenCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        system = serializer.validated_data['system']
        token_value = TokenService().create(system=system)
        return Response({'token': {'value': token_value, 'system': system}}, status=status.HTTP_201_CREATED)
