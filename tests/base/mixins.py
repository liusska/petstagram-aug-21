from petstagram.pets.models import Pet
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class PetTestUtils:
    def create_pet(self, **kwargs):
        return Pet.objects.create(**kwargs)


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)
