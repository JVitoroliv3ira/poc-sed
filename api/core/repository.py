from typing import Type, TypeVar, Generic, Optional, List

from django.db import models

T = TypeVar('T', bound=models.Model)


class BaseRepository(Generic[T]):
    model: Type[T]

    def __init__(self, model: Type[T]):
        self.model = model

    def get(self, id: int) -> Optional[T]:
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            return None

    def get_all(self) -> List[T]:
        return self.model.objects.all()

    def create(self, **kwargs) -> T:
        return self.model.objects.create(**kwargs)

    def update(self, id: int, **kwargs) -> Optional[T]:
        obj = self.get(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None

    def delete(self, id: int) -> bool:
        obj = self.get(id)
        if obj:
            obj.delete()
            return True
        return False
