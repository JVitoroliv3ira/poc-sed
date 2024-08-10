from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.emails.serializers import EmailSerializer
from apps.emails.service import EmailService
from apps.tokens.service import TokenService


class SendEmailView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.headers.get('X-TOKEN-EMAIL-SENDER')
        if not token or not TokenService().validate_token(token):
            return Response(
                {'detail': 'Token inválido ou ausente.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = EmailSerializer(data=request.data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        EmailService().send_emails(serializer.validated_data)

        return Response(
            {'message': 'Todos os emails foram enviados com sucesso.'},
            status=status.HTTP_200_OK
        )
