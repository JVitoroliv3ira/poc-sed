from apps.tokens.models import Token
from core.repository import BaseRepository


class TokenRepository(BaseRepository[Token]):
    def __init__(self) -> None:
        super().__init__(Token)
