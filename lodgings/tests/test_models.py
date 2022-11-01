from django.test import TestCase
from ..models import Lodging, LodgingCategories


class TestModels (TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.lodging_datas = [
            {
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

    def test_category_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('category').max_length
            self.assertEqual(max_length, 20)

    def test_category_choices(self):
        for lodging in self.lodgings:
            choices = lodging._meta.get_field('sex').choices
            self.assertEqual(choices, LodgingCategories.choices)

    def test_name_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('name').max_length
            self.assertEqual(max_length, 127)

    def test_state_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('state').max_length
            self.assertEqual(max_length, 20)

    def test_city_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('city').max_length
            self.assertEqual(max_length, 127)

    def test_district_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('district').max_length
            self.assertEqual(max_length, 127)

    def test_district_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('district').max_length
            self.assertEqual(max_length, 127)

    def test_street_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('street').max_length
            self.assertEqual(max_length, 127)

    def test_number_max_length(self):
        self.lodging_datas[0]["number"] = 0
        lodging = Lodging.objects.create(**self.lodging_datas[0])
        self.assertEqual(lodging.number, 0)

    def test_complement_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('complement').max_length
            self.assertEqual(max_length, 30)

    def test_cep_max_length(self):
        for lodging in self.lodgings:
            max_length = lodging._meta.get_field('cep').max_length
            self.assertEqual(max_length, 8)
