from django.test import TestCase , SimpleTestCase
from django.urls import reverse

# Create your tests here

class TestViewUsesCorrectTemplate(SimpleTestCase):

 def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('posts'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
