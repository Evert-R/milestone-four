from django.test import TestCase
from django.contrib.auth.models import User, Group
from works.models import categories


class TestDashboardAttributesViews(TestCase):

    def setUp(self):
        group = Group.objects.create(name='admin')
        user = User.objects.create_user(
            username='username', password='password')
        group.user_set.add(user)
        self.client.login(username='username', password='password')

    def test_add_category(self):
        response = self.client.post(
            '/dashboard/addcategory/', {'category': 'test',
                                        'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)
        self.assertTrue(categories.objects.exists())
        self.assertRedirects(response, '/dashboard/addwork/')
