from typing import Optional

from apps.tokens.models import Token
from core.repository import BaseRepository


class TokenRepository(BaseRepository[Token]):
    def __init__(self) -> None:
        super().__init__(Token)

    def get_by_hash(self, hash: str) -> Optional[Token]:
        try:
            return self.model.objects.get(hash=hash)
        except self.model.DoesNotExist:
            return None
