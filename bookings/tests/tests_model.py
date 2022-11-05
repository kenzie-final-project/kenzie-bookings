from django.test import TestCase
from accounts.models import Account
from lodgings.models import Lodging
from rooms.models import Room
from ..models import Booking


class BookingModelTest(TestCase):
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
                "description": "description",
                "name": "Tetris Container",
                "state": "Paraná",
                "city": "Foz do Iguaçu",
                "district": "Vila Yolanda",
                "street": "Av. das Cataratas",
                "number": "639",
                "complement": "complement",
                "cep": "85853000"
            },
            {
                "host": cls.account.id,
                "category": "Hotel",
                "description": "description",
                "name": "Ibis Styles",
                "state": "São Paulo",
                "city": "São Paulo",
                "district": "Centro",
                "street": "Avenida Senador Queiros",
                "number": "202",
                "complement": "complement",
                "cep": "01026000"
            }
        ]
        cls.lodgings = [Lodging.objects.create(**lodging_data) for lodging_data in cls.lodging_datas]

        cls.room_datas = [
            {
                "number": 1,
                "cost": 100.00,
                "occupation": 2,
                "available": True,
                "description": "Quarto com cama de casal",
                "lodging": cls.lodgings[0].id
            },
            {
                "number": 2,
                "cost": 150.00,
                "occupation": 3,
                "available": True,
                "description": "Quarto com cama de casal e cama de solteiro",
                "lodging": cls.lodgings[0].id
            }
        ]
        cls.rooms = [Room.objects.create(**room_data) for room_data in cls.room_datas]

        cls.booking_data = {
            "checkin_date": "2021-01-01",
            "checkout_date": "2021-01-02",
            "cost": 100.00,
            "account": cls.account.id,
            "room": cls.rooms[0].id
        }
        cls.booking = Booking.objects.create(**cls.booking_data)

    def test_cost_max_digits(self):
        max_digits = self.booking._meta.get_field("cost").max_digits
        self.assertEqual(max_digits, 10)

    def test_cost_decimal_places(self):
        decimal_places = self.booking._meta.get_field("cost").decimal_places
        self.assertEqual(decimal_places, 2)
