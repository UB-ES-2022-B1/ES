from django.test import TestCase

# Create your tests here.
from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from django.test import Client as cl
from .models import Client
import json

class ClientTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new client object.
        """

        data = {'name': 'Lucas',
                'surname': 'Garcia',
                'password': 'ASD1235',
                'email': 'mailfalso1@yahoo.com',
                'phone': '123091243',
                'country': 'Argentina',
                'birthdate': '1987-06-12'}

        response = self.client.post('http://localhost:8000/accounts/register', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get(email='mailfalso1@yahoo.com').name, 'Lucas')

    def test_log_in(self):
        """
            Ensure we can log in and the tocken is created
            Ensure that the counter for wrong paswords works as intended
            Ensure that once the pasword has been written wrong 5 times, the account is blocket for good
        """
        # first register two users

        data_registro1 = {"name": 'mail',
                          'surname': 'falso1',
                          'password': 'ASD1235',
                          'email': 'mailfalso23@yahoo.com',
                          'phone': '123091243',
                          'country': 'Argentina',
                          'birthdate': '1987-06-12'}
        data_registro2 = {'name': 'mail',
                          'surname': 'falso2',
                          'password': 'ASD1235',
                          'email': 'mailfalso24@yahoo.com',
                          'phone': '123091243',
                          'country': 'Narnia',
                          'birthdate': '1987-06-12'}
        self.client.post('http://localhost:8000/accounts/register', data_registro1, format='json')
        self.client.post('http://localhost:8000/accounts/register', data_registro2, format='json')
        self.assertEqual(Client.objects.count(), 2)

        data_good = {"email": "mailfalso24@yahoo.com",
                     "password": "ASD1235"}
        data_bad = {'email': 'mailfalso23@yahoo.com',
                    'password': '1111111'}

        # Ensure that the counter for wrong paswords works as intended
        response = self.client.post('http://localhost:8000/accounts/login', data_bad, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Client.objects.get(email=data_bad['email']).failedLoginAttemps, 1)

        # Let's block the account
        for n in [2, 3, 4, 5]:
            response = self.client.post('http://localhost:8000/accounts/login', data_bad,
                                        format='json')
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(Client.objects.get(email=data_bad['email']).failedLoginAttemps, n)
        response = self.client.post('http://localhost:8000/accounts/login', data_bad,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Let's log in correctly
        response = self.client.post('http://localhost:8000/accounts/login', data_good,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_veure_perfil(self):
        """"
        Test to see user profile
        """

        data_registro2 = {"name": "Enrique",
                          "surname": "falso2",
                          "password": "ASD1235",
                          "email": "mailfalso24@yahoo.com",
                          "phone": "123091243",
                          "country": "Narnia",
                          "birthdate": "1987-06-12"}

        self.client.post('http://127.0.0.1:8000/accounts/register', data_registro2, format='json')

        data_good = {"email": "mailfalso24@yahoo.com",
                     "password": "ASD1235"}
        response = self.client.post('http://localhost:8000/accounts/login', data_good, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.json()['access']

        mail = {"email": "mailfalso24@yahoo.com"}
        response = self.client.post('http://localhost:8000/accounts/get-profile', mail, format='json',
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['msg']['name'], "Enrique")

    def test_login_token(self):

        data_registro1 = {"name": 'mail',
                          'surname': 'falso1',
                          'password': 'ASD1235',
                          'email': 'mailfalso23@yahoo.com',
                          'phone': '123091243',
                          'country': 'Argentina',
                          'birthdate': '1987-06-12'}

        data_house = {
            "title": "casa1",
            "owner": "mailfalso1@yahoo.com",
            "description": "bonica",
            "location": "Tarragona",
            "base_price": "100",
            "extra_costs": "10",
            "taxes": "4",
            "num_hab": "4",
            "num_beds": "8",
            "num_bathrooms": "4",
            "num_people": "10",
            "company_individual": "particular",
            "kitchen": "True",
            "swiming_pool": "True",
            "garden": "True",
            "billar_table": "True",
            "gym": "True",
            "TV": "True",
            "WIFII": "True",
            "dishwasher": "True",
            "washing_machine": "True",
            "air_conditioning": "False",
            "free_parking": "False",
            "spacious": "False",
            "central": "False",
            "quite": "False",
            "alarm": "False",
            "smoke_detector": "False",
            "health_kit": "False"

        }

        self.client.post('http://localhost:8000/accounts/register', data_registro1, format='json')

        data_good = {"password": "ASD1235", "email": "mailfalso23@yahoo.com"}
        response = self.client.post('http://127.0.0.1:8000/accounts/login', data_good, format='json')
        token = response.json()['access']

        response = self.client.post('http://127.0.0.1:8000/houses/register', data=data_house,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
