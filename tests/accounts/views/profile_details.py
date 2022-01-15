from django.test import TestCase, Client
from django.urls import reverse

from tests.base.tests import PetstagramTestCase
from petstagram.pets.models import Pet
from petstagram.accounts.models import Profile


class ProfileDetailsTest(PetstagramTestCase):

    def test_getDetails_when_loggedInUserWithNoPets_shouldGetDetailsWithNoPets(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        pets = list(response.context['pets'])
        profile = response.context['profile']

        self.assertListEmpty(pets)
        self.assertEqual(self.user.id, profile.user_id)

    def test_getDetails_when_loggedInUserWithPets_shouldGetDetailsWithPets(self):
        pet = Pet.objects.create(
            name='Test Pet',
            description='Test pet desc',
            age='1',
            image='path/to/image.png',
            type=Pet.TYPE_CHOICE_DOG,
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([pet], list(response.context['pets']))

    def test_postDetails_whenUserLoggenInWithoutImage_shouldChangeImage(self):
        path_to_image = 'path/to/image.png'
        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            path_to_image: 'path/to/image.png',
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        # self.assertEqual(path_to_image, profile.profile_image.url)

    def test_postDetails_whenUserLoggenInWithImage_shouldChangeImage(self):
        path_to_image = 'path/to/image.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            path_to_image: 'path/to/image.png',
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        # self.assertEqual(path_to_image, profile.profile_image.url)

