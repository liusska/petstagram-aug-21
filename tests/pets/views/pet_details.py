from tests.base.tests import PetstagramTestCase
from tests.base.mixins import PetTestUtils, UserTestUtils
from petstagram.pets.models import Pet, Like

from django.test import TestCase, Client
from django.urls import reverse


class ProfileDetailsTest(PetTestUtils, UserTestUtils, PetstagramTestCase):
    def test_getPetDetails_whenPetExistsAndIsOwner_shouldReturnDetailsFormOwner(self):
        pass

    def test_getPetDetails_whenPetNotExistsAndIsOwner_shouldReturnDetailsFormOwner(self):
        self.client.force_login(self.user)
        pet = self.create_pet(
            name='Test Pet',
            description='Test pet desc',
            age='1',
            image='path/to/image.png',
            type=Pet.TYPE_CHOICE_DOG,
            user=self.user,
        )

        response = self.client.get(reverse('details pets', kwargs={
            'pk': pet.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPetDetails_whenPetExistsAndIsNotOwnerAndNotLiked_shouldReturnDetailsFormOwner(self):
        self.client.force_login(self.user)
        pet_owner = self.create_user(email='pet@user.bg', password='123456')

        pet = self.create_pet(
            name='Test Pet',
            description='Test pet desc',
            age='1',
            image='path/to/image.png',
            type=Pet.TYPE_CHOICE_DOG,
            user=pet_owner,
        )

        response = self.client.get(reverse('details pets', kwargs={
            'pk': pet.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPetDetails_whenPetExistsAndIsNotOwnerAndLiked_shouldReturnDetailsFormOwner(self):
        self.client.force_login(self.user)
        pet_owner = self.create_user(email='pet@user.bg', password='123456')

        pet = self.create_pet(
            name='Test Pet',
            description='Test pet desc',
            age='1',
            image='path/to/image.png',
            type=Pet.TYPE_CHOICE_DOG,
            user=pet_owner,
        )
        Like.objects.create(
            pet=pet,
            user=self.user,
        )

        response = self.client.get(reverse('details pets', kwargs={
            'pk': pet.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])

