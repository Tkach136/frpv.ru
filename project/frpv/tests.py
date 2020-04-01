from django.test import TestCase

from .models import Info


class NavDetailListTests(TestCase):

    def test_has_objects_exists(self, header='navigator'):
        """тест проверяет, существуют ли объекты"""
        qs = Info.objects.filter(header=header)
        self.assertIsNotNone(qs)
        print(qs)

    def test_has_skolkovo_exists(self):
        """тест проверяет, сколько объектов существует"""
        qs = Info.objects.all()
        self.assertEqual(qs.count(), 9)

