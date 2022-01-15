from django.test import TestCase, Client
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class PetstagramTestCase(TestCase):
    logged_in_user_email = 'liusska@mail.bg'
    logged_in_user_password = '123456'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
