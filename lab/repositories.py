from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from lab.models import Category

class BaseRepository:
    model = None  # to be overridden by child classes

    @classmethod
    def get(cls, pk):
        try:
            return cls.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def create(cls, **kwargs):
        return cls.model.objects.create(**kwargs)

    @classmethod
    def update(cls, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def delete(cls, instance):
        instance.delete()

    @classmethod
    def all(cls):
        return cls.model.objects.all()

class UserRepository(BaseRepository):
    model = get_user_model()

class CategoriesRepository(BaseRepository):
    model = Category


