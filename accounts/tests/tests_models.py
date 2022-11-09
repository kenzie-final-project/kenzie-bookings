from django.test import TestCase
from ..models import Account


class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account_data = {
            "username": "username",
            "password": "password",
            "first_name": "name",
            "last_name": "last_name",
            "email": "email@email.com",
            "phone": "123456789012",
            "is_host": True,
            "cpf": "12345678901"
        }

        cls.account = Account.objects.create_user(**cls.account_data)

    def test_username_attr(self):
        username = self.account._meta.get_field('username')
        max_length = username.max_length

        self.assertEqual(max_length, 150)

    def test_email_attr(self):
        email = self.account._meta.get_field('email')
        max_length = email.max_length

        self.assertEqual(max_length, 254)

    def test_phone_attr(self):
        phone = self.account._meta.get_field('phone')
        max_length = phone.max_length

        self.assertEqual(max_length, 12)

    def test_cpf_attr(self):
        cpf = self.account._meta.get_field('cpf')
        max_length = cpf.max_length

        self.assertEqual(max_length, 11)
