from django.test import TestCase
from django.urls import resolve
from twitter.views import index
from django.http import HttpRequest


# Create your tests here.

class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_corrects_html(self):
        request = HttpRequest
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Twitter</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
