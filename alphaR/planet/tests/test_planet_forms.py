from django.test import TestCase

from alphaR.planet.forms.planet_forms import PlanetForm


class PlanetFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'name': 'Terra',
            'chemical_elements': 'Oxigênio, Nitrogênio',
            'percentage_of_water': 71,
            'alphaR_distance': 149,
            'probability_of_life': 'Provável'
        }
        form = PlanetForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'chemical_elements': 'Oxigênio, Nitrogênio',
            'percentage_of_water': 10,
            'alphaR_distance': -149.6,
            'probability_of_life': 'yes'
        }
        form = PlanetForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
