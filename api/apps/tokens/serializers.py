from rest_framework import serializers


class TokenCreateSerializer(serializers.Serializer):
    system = serializers.CharField(
        max_length=50,
        required=True,
        error_messages={
            'required': 'O campo sistema é obrigatório.',
            'blank': 'O campo sistema é obrigatório.',
            'max_length': 'O nome do sistema não pode ter mais que 50 caracteres.'
        }
    )
