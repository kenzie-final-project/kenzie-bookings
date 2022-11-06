from rest_framework.test import APITestCase
from accounts.models import Account
from lodgings.models import Lodging


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

        cls.host = Account.objects.create_user(**host)

        lodging = {
            "name": "XXX",
            "category": "Resort",
            "description": "Bom",
            "state": "SP",
            "city": "São Paulo",
            "district": "bira",
            "street": "rua rua",
            "number": 77,
            "cep": "12345678"
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
            "cep": "12345678"
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
            "category": "Hotel",
            "description": "Mal",
            "state": "SPx",
            "city": "São Paulox",
            "district": "bira",
            "street": "rua rua",
            "number": 778,
            "cep": "12345678"
        }

        response = self.client.post('/api/lodgings/', lodging, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], "ZZZ")

