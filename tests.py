import unittest
import requests

class TestApi(unittest.TestCase):
    def test_without_filters(self):
        resp = requests.get('http://localhost:8084/get_properties')
        self.assertEqual(200,resp.status_code)

    def test_city_filter(self):
        resp = requests.get('http://localhost:8084/get_properties?city=bogota')
        self.assertEqual(200,resp.status_code)

    def test_status_filter(self):
        resp = requests.get('http://localhost:8084/get_properties?status=vendido')
        self.assertEqual(200,resp.status_code)

    def test_year_filter(self):
        resp = requests.get('http://localhost:8084/get_properties?year=2020')
        self.assertEqual(200,resp.status_code)

    def test_multiple_filters(self):
        resp = requests.get('http://localhost:8084/get_properties?year=2020&status=vendido&city=bogota')
        self.assertEqual(200,resp.status_code)
    

if __name__ == "__main__":
    unittest.main()
