from rest_framework.test import APITestCase
from accounts.models import Account
from lodgings.models import Lodging
from rooms.models import Room
from bookings.models import Booking

class BookingViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.account_data = {
            "username": "user",
            "password": "password",
            "first_name": "name",
            "last_name": "last_name",
            "email": "email@email.com",
            "phone": "123456789012",
            "is_host": True,
            "cpf": "12345678901"
        }
        cls.account = Account.objects.create_user(**cls.account_data)

        cls.user_data = {
            "username": "dundun",
            "password": "password",
            "first_name": "name",
            "last_name": "last_name",
            "email": "email2@email.com",
            "phone": "123456789012",
            "is_host": False,
            "cpf": "12345678902"
        }
        cls.user = Account.objects.create_user(**cls.user_data)

        cls.lodging_datas = [
            {
                "host": cls.account,
                "category": "pousada",
                "description": "description",
                "name": "Tetris Container",
                "state": "Paraná",
                "city": "Foz do Iguaçu",
                "district": "Vila Yolanda",
                "street": "Av. das Cataratas",
                "number": "639",
                "complement": "complement",
                "cep": "85853000",
                "phone": "22224444",
                "email": "email@email.com"
            },
            {
                "host": cls.account,
                "category": "hotel",
                "description": "description",
                "name": "Ibis Styles",
                "state": "São Paulo",
                "city": "São Paulo",
                "district": "Centro",
                "street": "Avenida Senador Queiros",
                "number": "202",
                "complement": "complement",
                "cep": "01026000",
                "phone": "22224444",
                "email": "email@email.com"
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
                "lodging": cls.lodgings[0]
            },
            {
                "number": 2,
                "cost": 150.00,
                "occupation": 3,
                "available": True,
                "description": "Quarto com cama de casal e cama de solteiro",
                "lodging": cls.lodgings[0]
            }
        ]
        cls.rooms = [Room.objects.create(**room_data) for room_data in cls.room_datas]

        cls.booking_data = {
            "checkin_date": "2021-01-01",
            "checkout_date": "2021-01-02",
            "cost": 100.00,
            "user": cls.account,
            "room": cls.rooms[0]
        }
        cls.booking = Booking.objects.create(**cls.booking_data)
    
    def test_if_user_can_make_a_booking(self):
        booker = {
            "username": self.user.username,
            "password": 'password',
        }

        token = self.client.post('/api/login/', booker, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        booking_data = {
            "checkin_date": "2022-11-30",
            "checkout_date": "2022-12-20",
            "cost": 50.00,
        }

        response = self.client.post(f'/api/lodgings/{self.rooms[0].lodging.id}/rooms/{self.rooms[0].id}/bookings/', booking_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['checkin_date'], "2022-11-30")

    def test_if_the_cost_is_being_calculated_correctly(self):
        booker = {
            "username": self.user.username,
            "password": 'password',
        }

        token = self.client.post('/api/login/', booker, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        booking_data = {
            "checkin_date": "2022-11-20",
            "checkout_date": "2022-11-30",
            "cost": 100.00,
        }

        response = self.client.post(f'/api/lodgings/{self.rooms[0].lodging.id}/rooms/{self.rooms[0].id}/bookings/', booking_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['cost'], '1000.00')

    def test_if_you_can_use_an_impossible_checkin_date(self):
        booker = {
            "username": self.user.username,
            "password": 'password',
        }

        token = self.client.post('/api/login/', booker, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.data['token'])

        booking_data = {
            "checkin_date": "2022-13-20",
            "checkout_date": "2022-14-30",
            "cost": 100.00,
        }

        response = self.client.post(f'/api/lodgings/{self.rooms[0].lodging.id}/rooms/{self.rooms[0].id}/bookings/', booking_data, format='json')
        self.assertEqual(response.status_code, 400)
