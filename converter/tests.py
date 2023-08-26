from django.test import SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_converter(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

