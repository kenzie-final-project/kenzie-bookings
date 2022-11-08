from rest_framework.test import APITestCase, APIClient

from ..models import Booking


class BookingTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.booking_data = {
            "checkin_date": "2022-11-30",
            "checkout_date": "2022-12-20",
            "cost": 50.00,
        }

        cls.booking = Booking.objects.create(**cls.booking_data)

