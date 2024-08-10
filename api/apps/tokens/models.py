from django.db import models


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=64, unique=True, editable=False)
    system = models.CharField(max_length=50)

    class Meta:
        db_table = 'tb_tokens'
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
