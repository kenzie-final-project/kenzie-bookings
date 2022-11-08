from rest_framework.test import APITestCase
from accounts.models import Account
from lodgings.models import Lodging
import ipdb


class LodgingsViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        host = {
            "first_name": "plinio",
            "last_name": "figueiredo",
            "email": "plinio@plinio.com",
            "username": "dunas",
            "password": "1234",
            "phone": "22224444",
            "cpf": "12345678911",
            "is_host": True
        }
        host2 = {
            "first_name": "plinio",
            "last_name": "figueiredo",
            "email": "plinio@plinio.com",
            "username": "plinio",
            "password": "1234",
            "phone": "22224444",
            "cpf": "12345678911",
            "is_host": True
        }

        user = {
            "first_name": "plinio",
            "last_name": "figueiredo",
            "email": "plinio@plinio.com",
            "username": "janjan",
            "password": "1234",
            "phone": "22224444",
            "cpf": "12345678911",
            "is_host": False
        }

        cls.user = Account.objects.create_user(**user)
        cls.host = Account.objects.create_user(**host)
        cls.host2 = Account.objects.create_user(**host2)

        lodging = {
            "name": "XXX",
            "category": "Resort",
            "description": "Bom",
            "state": "SP",
            "city": "São Paulo",
            "district": "bira",
            "street": "rua rua",
            "number": 77,
            "cep": "12345678",
            "phone": "22224444",
            "email": "email@email.com"
        }

        lodging2 = {
            "name": "YYY",
            "category": "Hotel",
            "description": "Mal",
            "state": "SP",
            "city": "São Paulo",
            "district": "bira",
            "street": "rua rua",
            "number": 77,
            "cep": "12345678",
            "phone": "22224445",
            "email": "email1@email.com"
        }

        cls.lodging1 = Lodging.objects.create(**lodging, host=cls.host)
        cls.lodging2 = Lodging.objects.create(**lodging2, host=cls.host)

    def test_if_host_can_create_a_lodging(self):
        user = {
            "username": "dunas",
            "password": "1234"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        lodging = {
            "name": "ZZZ",
            "category": "hotel",
            "description": "Mal",
            "state": "SPx",
            "city": "São Paulox",
            "district": "bira",
            "street": "rua rua",
            "number": 778,
            "cep": "12345678",
            "phone": "22224446",
            "email": "email2@email.com"
        }

        response = self.client.post('/api/lodgings/', lodging, format='json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], "ZZZ")

    def test_if_non_host_can_create_a_lodging(self):
        user = {
            "username": "janjan",
            "password": "1234"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        lodging = {
            "name": "ZZZ",
            "category": "hotel",
            "description": "Mal",
            "state": "SPx",
            "city": "São Paulox",
            "district": "bira",
            "street": "rua rua",
            "number": 778,
            "cep": "12345678",
            "phone": "22224447",
            "email": "email3@email.com"
        }

        response = self.client.post('/api/lodgings/', lodging, format='json')

        self.assertEqual(response.status_code, 403)

    def test_if_host_can_update_a_lodging(self):
        user = {
            "username": "dunas",
            "password": "1234"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        lodging = {
            "name": "ZZZ22",
        }

        response = self.client.patch(f'/api/lodgings/{self.lodging1.id}/', lodging, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'ZZZ22')

    def test_if_another_host_can_update_a_lodging(self):
        user = {
            "username": "plinio",
            "password": "1234"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        lodging = {
            "name": "ZZZ22",
        }

        response = self.client.patch(f'/api/lodgings/{self.lodging1.id}/', lodging, format='json')

        self.assertEqual(response.status_code, 403)

    def test_if_host_can_delete_a_lodging(self):
        user = {
            "username": "dunas",
            "password": "1234"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        lodging = {
            "name": "ZZZ22",
        }

        response = self.client.delete(f'/api/lodgings/{self.lodging1.id}/', lodging, format='json')

        self.assertEqual(response.status_code, 204)

    def test_if_another_host_can_delete_a_lodging(self):
        user = {
            "username": "plinio",
            "password": "1234"
        }
        token = self.client.post('/api/login/', user, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        lodging = {
            "name": "ZZZ22",
        }

        response = self.client.delete(f'/api/lodgings/{self.lodging1.id}/', lodging, format='json')

        self.assertEqual(response.status_code, 403)
