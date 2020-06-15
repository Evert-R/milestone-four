from django.test import TestCase

# Create your tests here.


class TestAboutViews(TestCase):

    def test_show_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
