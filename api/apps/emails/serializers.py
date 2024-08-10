from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(
        max_length=255,
        required=True,
        error_messages={
            'required': 'O campo assunto é obrigatório.',
            'max_length': 'O assunto não pode exceder 255 caracteres.',
        }
    )
    recipients = serializers.CharField(
        required=True,
        error_messages={
            'required': 'O campo destinatários é obrigatório.',
            'invalid': 'O formato dos destinatários é inválido.'
        }
    )
    body = serializers.CharField(
        required=False,
        allow_blank=True,
        error_messages={
            'invalid': 'O campo corpo do email contém caracteres inválidos.'
        }
    )

    def validate_recipients(self, value):
        emails = value.split(',')
        for email in emails:
            email = email.strip()
            try:
                serializers.EmailField().run_validation(email)
            except serializers.ValidationError:
                raise serializers.ValidationError(f'O email {email} não é válido.')
        return value
