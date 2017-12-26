from django.test import TestCase
from django.urls import resolve
from twitter.views import index
from django.http import HttpRequest
from django.template.loader import render_to_string


# Create your tests here.

class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_corrects_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('twitter/index.html')
        self.assertEqual(response.content.decode(), expected_html)
