from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.test import TestCase
from .forms import LogInForm, RegisterForm, UserUpdateForm, UserDetailsForm
from shop.models import shipping


class TestLoginForm(TestCase):
    def test_all_fields(self):
        form = LogInForm({'username': 'test',
                          'password': 'GGiuyox!ghy874yt378y9875'})
        self.assertTrue(form.is_valid())

    def test_no_fields(self):
        form = LogInForm({'username': '',
                          'password': ''})
        self.assertFalse(form.is_valid())


class TestRegisterForm(TestCase):
    def test_all_fields(self):
        form = RegisterForm({'username': 'test',
                             'first_name': 'test',
                             'last_name': 'test',
                             'email': 'test@test.nl',
                             'password1': 'testPassword23!',
                             'password2': 'testPassword23!'})
        self.assertTrue(form.is_valid())

    def test_required_fields(self):
        form = RegisterForm({'username': 'test',
                             'password1': 'testPassword23!',
                             'password2': 'testPassword23!'})
        self.assertTrue(form.is_valid())

    def test_no_required_fields(self):
        form = RegisterForm({'first_name': 'test',
                             'last_name': 'test',
                             'email': 'test@test.nl'
                             })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertIn('password1', form.errors.keys())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['username']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['password1']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['password2']
                         [0], 'This field is required.')

    def test_passwords_no_match(self):
        form = RegisterForm({'username': 'test',
                             'first_name': 'test',
                             'last_name': 'test',
                             'email': 'test@test.nl',
                             'password1': 'testPassword23!',
                             'password2': 'testPassword24!'})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2']
                         [0], 'The two password fields didn’t match.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test if only fields in the Meta class are displayed
        """
        form = RegisterForm()
        self.assertEqual(form.Meta.fields, ['username', 'first_name', 'last_name',
                                            'email', 'password1', 'password2'])


class TestUserUpdateForm(TestCase):
    def test_all_fields(self):
        form = UserUpdateForm({'username': 'test',
                               'first_name': 'test',
                               'last_name': 'test',
                               'email': 'test@test.nl'
                               })
        self.assertTrue(form.is_valid())

    def test_no_required_fields(self):
        form = UserUpdateForm({'username': '',
                               'first_name': 'test',
                               'last_name': 'test',
                               'email': 'test@test.nl'
                               })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username']
                         [0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test if only fields in the Meta class are displayed
        """
        form = UserUpdateForm()
        self.assertEqual(form.Meta.fields, ['username', 'first_name', 'last_name',
                                            'email'])


class TestUserDetailsForm(TestCase):

    def test_all_fields(self):
        # Get user object
        user = User.objects.create_user(
            username='username', password='password')
        ship = shipping.objects.create(region='test', price=50)
        form = UserDetailsForm({'user': user.pk,
                                'address1': 'test',
                                'address2': 'test',
                                'postcode': 'test',
                                'city': 'test',
                                'country': 'test',
                                'telephone': 'test',
                                'shipping': ship.pk
                                })
        self.assertTrue(form.is_valid())

    def test_no_required_fields(self):

        form = UserDetailsForm({'address1': '',
                                'address2': '',
                                'postcode': '',
                                'city': '',
                                'country': '',
                                'telephone': '',
                                'shipping': ''
                                })
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors.keys())
        self.assertIn('address1', form.errors.keys())
        self.assertIn('postcode', form.errors.keys())
        self.assertIn('city', form.errors.keys())
        self.assertIn('country', form.errors.keys())
        self.assertIn('shipping', form.errors.keys())
        self.assertEqual(form.errors['user']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['address1']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['postcode']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['city']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['country']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['shipping']
                         [0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test if only fields in the Meta class are displayed
        """
        form = UserDetailsForm()
        self.assertEqual(form.Meta.fields, ['user', 'address1', 'address2', 'postcode',
                                            'city', 'country', 'telephone', 'shipping'])
