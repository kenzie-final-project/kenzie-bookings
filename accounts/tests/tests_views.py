from accounts.models import Account
from rest_framework.test import APITestCase


class AccountViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account_data = {
            "username": "username",
            "password": "password",
            "first_name": "name",
            "last_name": "last_name",
            "email": "email@email.com",
            "phone": "123456789012",
            "is_host": False,
            "cpf": "12345678901"
        }

        cls.account = Account.objects.create_user(**cls.account_data)

    def test_patch_user(self):
        user = {
            "username": "username",
            "password": "password"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        patch_account = {
            "username": "username2"
        }

        response = self.client.patch(f'/api/accounts/{self.account.id}', patch_account, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], "username2")

    def test_delete_user(self):
        user = {
            "username": "username",
            "password": "password"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        response = self.client.delete(f'/api/accounts/{self.account.id}')
        
        self.assertEqual(response.status_code, 204)

    def test_if_user_can_change_is_user_field(self):
        user = {
            "username": "username",
            "password": "password"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        patch_account = {
            "is_host": True
        }

        response = self.client.patch(f'/api/accounts/{self.account.id}', patch_account, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['is_host'], False)
