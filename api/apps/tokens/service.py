import hashlib
import secrets

from apps.tokens.repository import TokenRepository


class TokenService:
    def __init__(self) -> None:
        self.token_repository = TokenRepository()

    def create(self, system: str) -> str:
        token_value = secrets.token_urlsafe(24)
        token_hash = hashlib.sha256(token_value.encode('utf-8')).hexdigest()
        self.token_repository.create(system=system, hash=token_hash)
        return token_value

    def validate_token(self, token_value: str) -> bool:
        token_hash = hashlib.sha256(token_value.encode('utf-8')).hexdigest()
        token = self.token_repository.get_by_hash(token_hash)
        return token is not None
