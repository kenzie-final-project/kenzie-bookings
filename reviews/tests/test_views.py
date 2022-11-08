from rest_framework.test import APITestCase
from ..models import Review
from lodgings.models import Lodging
from rooms.models import Room
from accounts.models import Account

class TestViews(APITestCase):
    @classmethod
    def setUpTestData(cls):
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

        user_data = {
            "username": "user",
            "password": "password",
            "first_name": "name",
            "last_name": "last_name",
            "email": "email@email.com",
            "phone": "123456789012",
            "is_host": False,
            "cpf": "99987654321"
        }

        cls.user = Account.objects.create_user(**user_data)

        cls.lodging_datas = [
            {
                "host": cls.account,
                "category": "Pousada",
                "name": "Tetris Container",
                "state": "Paraná",
                "city": "Foz do Iguaçu",
                "district": "Vila Yolanda",
                "street": "Av. das Cataratas",
                "number": "639",
                "cep": "85853000"
            },
            {
                "host": cls.account,
                "category": "Hotel",
                "name": "Ibis Styles",
                "state": "São Paulo",
                "city": "São Paulo",
                "district": "Centro",
                "street": "Avenida Senador Queiros",
                "number": "202",
                "cep": "01026000"
            }
        ]
        cls.lodgings = [Lodging.objects.create(**lodging_data) for lodging_data in cls.lodging_datas]

        cls.room_datas = [
            {
                "lodging": cls.lodgings[0],
                "cost": 10,
                "occupation": 2,
                "available": True,
                "description": "Quarto agradavel...",
            },
            {
                "lodging": cls.lodgings[0],
                "cost": 15,
                "occupation": 1,
                "available": True,
                "description": "Quarto ruim...",
            }
        ]
        cls.rooms = [Room.objects.create(**room_data) for room_data in cls.room_datas]

        cls.review_datas = [
            {
                "user": cls.account,
                "room": cls.rooms[0],
                "title": "Gostei, é mt bão",
                "review": "Gostei demais, é bem legal...",
                "stars": "5"
            },
            {
                "user": cls.account,
                "room": cls.rooms[1],
                "title": "Tem cheiro azedo e é sujo",
                "review": "Não gostei pq...",
                "stars": "1"
            }
        ]
        cls.reviews = [Review.objects.create(**review_data) for review_data in cls.review_datas]

        def test_if_an_user_can_create_a_review(self):
            user = {
            "username": "user",
            "password": "password"
            }
            token = self.client.post('/api/login/', user, format='json')
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

            review = {
                "title": "Gostei, é mt bão",
                "review": "Gostei demais, é bem legal...",
                "stars": "5"
            }

            response = self.client.post(f'lodgings/{self.lodgings[0]}/rooms/{self.rooms[0]}/reviews/', review, format='json')

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.data['stars'], "5")