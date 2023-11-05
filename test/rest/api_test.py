import http.client
import os
import unittest
from urllib.request import urlopen
import requests

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

def consumir_api(url):
    """
    Función que realiza una solicitud a una API y devuelve la respuesta.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción en caso de código de estado no exitoso
        return response.json()  # Suponiendo que la respuesta es en formato JSON
    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud, por ejemplo, conexión fallida, timeout, etc.
        print(f"Error en la solicitud a {url}: {e}")
        return e

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add_status(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_add_content(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            float(response.read()), 4, f"Error en la petición API a {url}"
        )

    def test_api_substract_status(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_substract_content(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            float(response.read()), 0, f"Error en la petición API a {url}"
        )

    def test_api_multiply_status(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_multiply_content(self):
        url = f"{BASE_URL}/calc/multiply/5/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
             float(response.read()), 20, f"Error en la petición API a {url}"
        )

    def test_api_divide_status(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_content(self):
        url = f"{BASE_URL}/calc/divide/4/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            float(response.read()), 2, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_content_error(self):
        url = f"{BASE_URL}/calc/divide/4/0"
        resultado = consumir_api(url)
        self.assertIn("BAD REQUEST", str(resultado), "La respuesta de la API tiene un error")


    def test_api_potentiation_status(self):
        url = f"{BASE_URL}/calc/potentiation/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_potentiation_content(self):
        url = f"{BASE_URL}/calc/potentiation/4/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            float(response.read()), 16, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt_status(self):
        url = f"{BASE_URL}/calc/sqrt/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt_content(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            float(response.read()), 2, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt_content_error(self):
        url = f"{BASE_URL}/calc/sqrt/0"
        resultado = consumir_api(url)
        self.assertIn("0.0", str(resultado), "La respuesta de la API tiene un error")

    def test_api_logarithm_status(self):
        url = f"{BASE_URL}/calc/logarithm/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_logarithm_content(self):
        url = f"{BASE_URL}/calc/logarithm/36"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            float(response.read()), 1.56, f"Error en la petición API a {url}"
        )
    
    def test_api_logarithm_content_error(self):
        url = f"{BASE_URL}/calc/logarithm/-1"
        resultado = consumir_api(url)
        self.assertIn("INTERNAL SERVER ERROR", str(resultado), "La respuesta de la API tiene un error")
       


