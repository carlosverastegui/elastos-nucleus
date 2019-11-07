from django.test import TestCase, Client
from django.urls import reverse
import json


class TestViews(TestCase):
    def test_generate_key_GET(self):
        client = Client()
        response = client.get(reverse("elastos_service:generateKey"))

        self.assertEquals(response.status_code, 200)
        #self.assertTemplateUsed(response, 'elastos_service/generateKey.html')
