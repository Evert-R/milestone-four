from django.test import TestCase
from django.contrib.auth.models import User, Group
from shop.models import shipping
from .models import user_details


class TestAccountsViews(TestCase):

    def setUp(self):
        # Create fake user and login
        group = Group.objects.create(name='admin')
        group = Group.objects.create(name='customer')
        user = User.objects.create_user(
            username='username', password='password')
        group.user_set.add(user)
        self.client.login(username='username', password='password')
        # Create a shipping object
        ship = shipping.objects.create(region='test', price=50)
        details = user_details.objects.create(user=user,
                                              address1='test',
                                              address2='test',
                                              postcode='test',
                                              city='test',
                                              country='test',
                                              telephone='test',
                                              shipping=ship)

    def test_show_profile(self):
        response = self.client.get('/accounts/profile/')
        self.assertTemplateUsed(response, 'profile.html')

    def test_update_user(self):
        active_user = User.objects.get(username='username')
        current_user_details = user_details.objects.get(user=active_user)
        ship = shipping.objects.first()
        response = self.client.post('/accounts/userupdate/',
                                    {'user': active_user.pk,
                                     'address1': 'test',
                                     'address2': 'test',
                                     'postcode': 'test',
                                     'city': 'test',
                                     'country': 'test',
                                     'telephone': 'test',
                                     'shipping': ship.pk,
                                     'next': '/accounts/profile/'
                                     }
                                    )
        self.assertRedirects(response, '/accounts/profile/')
        self.assertEqual(302, response.status_code)

    def test_show_register(self):
        response = self.client.get('/accounts/register/')
        self.assertTemplateUsed(response, 'register.html')

    def test_register_user(self):
        response = self.client.post('/accounts/register/',
                                    {'username': 'test',
                                     'first_name': 'test',
                                     'last_name': 'test',
                                     'email': 'test@test.nl',
                                     'password1': 'testPassword23!',
                                     'password2': 'testPassword23!',
                                     'next': '/accounts/profile/'}
                                    )
        self.assertEqual(302, response.status_code)
        self.assertTrue(User.objects.filter(username='test').exists())
        self.assertRedirects(response, '/accounts/profile/')

    def test_show_user_details(self):
        response = self.client.get('/accounts/userdetails/')
        self.assertTemplateUsed(response, 'userdetails.html')

    def test_add_user_details(self):
        active_user = User.objects.get(username='username')
        ship = shipping.objects.first()
        response = self.client.post('/accounts/userdetails/',
                                    {'user': active_user.pk,
                                     'address1': 'testnow',
                                     'address2': 'test',
                                     'postcode': 'test',
                                     'city': 'test',
                                     'country': 'test',
                                     'telephone': 'test',
                                     'shipping': ship.pk,
                                     'next': '/accounts/profile/'
                                     }
                                    )
        self.assertEqual(302, response.status_code)
        self.assertTrue(user_details.objects.filter(
            address1='testnow').exists())
        self.assertRedirects(response, '/accounts/profile/')

    def test_log_out(self):
        user = User.objects.get(username='username')
        response = self.client.get('/accounts/logout/')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_log_in(self):
        self.client.logout()
        user = User.objects.get(username='username')
        response = self.client.post('/accounts/login/',
                                    {'username': 'username',
                                     'password': 'password',
                                     'next': '/accounts/profile/'}
                                    )
        self.assertIn('_auth_user_id', self.client.session)
        self.assertRedirects(response, '/accounts/profile/')

    def test_show_login(self):
        self.client.logout()
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'login.html')
