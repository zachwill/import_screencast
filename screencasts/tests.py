"""Tests for screencasts."""

from django.test import TestCase


class TestScreencasts(TestCase):

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
