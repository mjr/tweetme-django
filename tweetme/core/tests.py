from django.test import TestCase
from django.shortcuts import resolve_url as r


# class HomeTest(TestCase):
#     def setUp(self):
#         self.response = self.client.get(r('home'))
#
#     def test_get(self):
#         """GET 'Home' must return status code 200"""
#         self.assertEqual(200, self.response.status_code)
#
#     def test_html(self):
#         """'Home' must use template index.html"""
#         self.assertTemplateUsed(self.response, 'index.html')