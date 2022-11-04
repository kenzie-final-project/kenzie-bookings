from django.test import TestCase
from accounts.models import Account
from lodgings.models import Lodging, LodgingCategories
from ..models import Room

class RoomModelTest(TestCase):
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
        cls.account = Account.objects.create(**cls.account_data)

        cls.lodging_datas = [
            {
                "host": cls.account.id,
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
                "host": cls.account.id,
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
        cls.lodgings = [Lodging.objects.create(**lodging_data) for lodging_data in cls.lodging_datas ]

        cls.room_datas = [
            {
                "number": 1,
                "cost": 100.00,
                "occupation": 2,
                "available": True,
                "description": "Quarto com cama de casal",
                "lodging": cls.lodging[0].id
            },
            {
                "number": 2,
                "cost": 150.00,
                "occupation": 3,
                "available": True,
                "description": "Quarto com cama de casal e cama de solteiro",
                "lodging": cls.lodging[0].id
            },
            {
                "number": 3,
                "cost": 200.00,
                "occupation": 4,
                "available": True,
                "description": "Quarto com cama de casal, cama de solteiro e cama auxiliar",
                "lodging": cls.lodging[0].id
            },
            {
                "number": 1,
                "cost": 100.00,
                "occupation": 2,
                "available": True,
                "description": "Quarto com cama de casal",
                "lodging": cls.lodging[1].id
            },
            {
                "number": 2,
                "cost": 150.00,
                "occupation": 3,
                "available": True,
                "description": "Quarto com cama de casal e cama de solteiro",
                "lodging": cls.lodging[1].id
            }
        ]
        cls.rooms = [Room.objects.create(**room_data) for room_data in cls.room_datas]

        def test_number_max_length(self):
            for room in self.rooms:
                max_length = room._meta.get_field('number').max_length
                self.assertEquals(max_length, 10)
                
        def test_cost_max_digits(self):
            for room in self.rooms:
                max_digits = room._meta.get_field('cost').max_digits
                self.assertEquals(max_digits, 20)

        def test_cost_decimal_places(self):
            for room in self.rooms:
                decimal_places = room._meta.get_field('cost').decimal_places
                self.assertEquals(decimal_places, 2)

        def test_occupation_max_length(self):
            for room in self.rooms:
                max_length = room._meta.get_field('occupation').max_length
                self.assertEquals(max_length, 10)
                
        def test_description_max_length(self):
            for room in self.rooms:
                max_length = room._meta.get_field('description').max_length
                self.assertEquals(max_length, 500)
       