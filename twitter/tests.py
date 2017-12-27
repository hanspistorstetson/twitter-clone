from django.test import TestCase
from django.urls import resolve
from twitter.views import index
from django.http import HttpRequest
from django.template.loader import render_to_string
import re


# Create your tests here.

def remove_csrf(html_code):
    csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
    return re.sub(csrf_regex, '', html_code)


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_corrects_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('twitter/index.html')
        self.assertEqual(remove_csrf(expected_html), remove_csrf(response.content.decode()))

    def test_index_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A tweet'

        response = index(request)

        self.assertIn('A tweet', response.content.decode())

        expected_html = render_to_string('twitter/index.html', {'new_item_text': 'A tweet'})
        self.assertEqual(remove_csrf(response.content.decode()), remove_csrf(expected_html))
