from django.test import TestCase
from django.urls import reverse

from alphaR.planet.models.planet import Planet


class ListPlanetsViewTestCase(TestCase):
    def test_list_planets_view(self):
        response = self.client.get(reverse('list_planets'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alphaR/list_planets.html')


class CreatePlanetViewTestCase(TestCase):
    def test_create_planet_view_get(self):
        response = self.client.get(reverse('create_planet'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alphaR/create_planet.html')

    def test_create_planet_view_post_valid_form(self):
        form_data = {
            'name': 'Terra',
            'chemical_elements': 'Oxigênio, Nitrogênio',
            'percentage_of_water': 70,
            'alphaR_distance': 150000000,
            'probability_of_life': 'Provável',
        }
        response = self.client.post(reverse('create_planet'), data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('list_planets'))
        self.assertEqual(form_data['name'], 'Terra')
        self.assertEqual(form_data['chemical_elements'], 'Oxigênio, Nitrogênio')
        self.assertEqual(form_data['percentage_of_water'], 70)
        self.assertEqual(form_data['alphaR_distance'], 150000000)
        self.assertEqual(form_data['probability_of_life'], 'Provável')

    def test_create_planet_view_post_invalid_form(self):
        form_data = {}
        response = self.client.post(reverse('create_planet'), data=form_data)

        self.assertEqual(response.status_code, 400)


class EditPlanetViewTestCase(TestCase):
    def setUp(self):
        self.planet = Planet.objects.create(
            name='Marte',
            chemical_elements='Dióxido de carbono',
            percentage_of_water=0,
            alphaR_distance=225000000,
            probability_of_life='Improvável',
        )

    def test_edit_planet_view_get(self):
        response = self.client.get(reverse('edit_planet', args=[self.planet.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alphaR/edit_planet.html')

    def test_edit_planet_view_post_valid_form(self):
        form_data = {
            'name': 'Marte',
            'chemical_elements': 'Dióxido de carbono',
            'percentage_of_water': 0,
            'alphaR_distance': 225000000,
            'probability_of_life': 'Provável',
        }
        response = self.client.post(reverse('edit_planet', args=[self.planet.pk]), data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('list_planets'))
        self.planet.refresh_from_db()
        self.assertEqual(self.planet.probability_of_life, 'Provável')

    def test_edit_planet_view_post_invalid_form(self):
        form_data = {}
        response = self.client.post(reverse('edit_planet', args=[self.planet.pk]), data=form_data)

        self.assertEqual(response.status_code, 400)
        self.planet.refresh_from_db()
        self.assertNotEqual(self.planet.probability_of_life, '')


class DeletePlanetViewTest(TestCase):
    def setUp(self):
        self.planet = Planet.objects.create(
            name='Marte',
            chemical_elements='Dióxido de carbono',
            percentage_of_water=0,
            alphaR_distance=225000000,
            probability_of_life='Improvável',
        )

    def test_delete_planet(self):
        response = self.client.post(reverse('delete_planet', args=[self.planet.pk]), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Planet.objects.filter(pk=self.planet.pk).exists())

    def test_delete_planet_get(self):
        response = self.client.get(reverse('delete_planet', args=[self.planet.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alphaR/delete_planet.html')
        self.assertEqual(response.context['planet'], self.planet)
