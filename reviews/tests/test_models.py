from django.test import TestCase
from ..models import Review
from lodgings.models import Lodging
from rooms.models import Room
from accounts.models import Account


class TestModels (TestCase):
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

    def test_title_max_length(self):
        for review in self.reviews:
            max_length = review._meta.get_field('title').max_length
            self.assertEqual(max_length, 255)

    def test_stars_max_value(self):
        self.lodging_datas[0]["number"] = 0
        lodging = Lodging.objects.create(**self.lodging_datas[0])
        self.assertNotEqual(lodging.number, 0)

    def test_stars_min_value(self):
        self.lodging_datas[0]["number"] = 6
        lodging = Lodging.objects.create(**self.lodging_datas[0])
        self.assertNotEqual(lodging.number, 6)
