"""Tests for screencasts."""

from django.test import TestCase
from mock import Mock, patch

from models import Screencast


class TestViews(TestCase):

    def test_home_page_is_working(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_is_working(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_redirect(self):
        response = self.client.get('/about', follow=True)
        self.assertTrue(response.redirect_chain)
        self.assertEqual(response.status_code, 200)

    def test_code_page_redirects(self):
        response = self.client.get('/code/')
        self.assertEqual(response.status_code, 302)

    def test_donate_page_is_working(self):
        response = self.client.get('/donate/')
        self.assertEqual(response.status_code, 200)

    @patch('screencasts.views.get_object_or_404')
    def test_screencast_page_looks_for_specific_one(self, get_object):
        self.client.get('/screencast/12345/')
        get_object.assert_called_with(Screencast, {'slug': '12345'})
