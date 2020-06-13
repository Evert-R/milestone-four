from django.test import TestCase
from django.contrib.auth.models import User, Group
from works.models import categories
from shop.models import work_types, work_sizes, materials, shipping


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

    def test_edit_category(self):
        # Create a category object
        categories.objects.create(name='test')
        # Get the category object
        category = categories.objects.first()
        response = self.client.post(
            f'/dashboard/editcategories/{category.pk}', {'category': 'testing',
                                                         'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)

    def test_edit_unknown_category(self):
        response = self.client.post(
            '/dashboard/editcategories/999', {'category': 'testing',
                                              'next': '/dashboard/addwork/'})
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_unknown_category_no_next(self):
        response = self.client.get('/dashboard/editcategories/999')
        self.assertRedirects(response, '/')

    def test_delete_category(self):
        # Create a category object
        categories.objects.create(name='test')
        # Get the category object
        category = categories.objects.first()
        response = self.client.get(f'/dashboard/editcategories/{category.pk}')
        self.assertFalse(categories.objects.exists())

    def test_add_work_type(self):
        response = self.client.post(
            '/dashboard/addworktype/', {'worktype': 'test',
                                        'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)
        self.assertTrue(work_types.objects.exists())
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_work_type(self):
        # Create a work_type object
        work_types.objects.create(name='test')
        # Get the category object
        work_type = work_types.objects.first()
        response = self.client.post(
            f'/dashboard/editworktypes/{work_type.pk}', {'worktype': 'testing',
                                                         'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)

    def test_edit_unknown_work_type(self):
        response = self.client.post(
            '/dashboard/editworktypes/999', {'worktype': 'testing',
                                             'next': '/dashboard/addwork/'})
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_unknown_work_type_no_next(self):
        response = self.client.get('/dashboard/editworktypes/999')
        self.assertRedirects(response, '/')

    def test_delete_work_type(self):
        # Create a work_type object
        work_types.objects.create(name='test')
        # Get the category object
        work_type = work_types.objects.first()
        response = self.client.get(f'/dashboard/editworktypes/{work_type.pk}')
        self.assertFalse(work_types.objects.exists())

    def test_add_work_size(self):
        response = self.client.post(
            '/dashboard/addworksize/', {'worksize': 'test',
                                        'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)
        self.assertTrue(work_sizes.objects.exists())
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_work_size(self):
        # Create a work_type object
        work_sizes.objects.create(name='test')
        # Get the category object
        work_size = work_sizes.objects.first()
        response = self.client.post(
            f'/dashboard/editworksizes/{work_size.pk}', {'worksize': 'testing',
                                                         'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)

    def test_edit_unknown_work_size(self):
        response = self.client.post(
            '/dashboard/editworksizes/999', {'worksize': 'testing',
                                             'next': '/dashboard/addwork/'})
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_unknown_work_size_no_next(self):
        response = self.client.get('/dashboard/editworksizes/999')
        self.assertRedirects(response, '/')

    def test_delete_work_size(self):
        # Create a work_type object
        work_sizes.objects.create(name='test')
        # Get the category object
        work_size = work_sizes.objects.first()
        response = self.client.get(f'/dashboard/editworksizes/{work_size.pk}')
        self.assertFalse(work_sizes.objects.exists())

    def test_add_material(self):
        response = self.client.post(
            '/dashboard/addmaterial/', {'material': 'test',
                                        'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)
        self.assertTrue(materials.objects.exists())
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_material(self):
        # Create a material object
        materials.objects.create(name='test')
        # Get the material object
        material = materials.objects.first()
        response = self.client.post(
            f'/dashboard/editmaterials/{material.pk}', {'material': 'testing',
                                                        'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)

    def test_edit_unknown_material(self):
        response = self.client.post(
            '/dashboard/editmaterials/999', {'material': 'testing',
                                             'next': '/dashboard/addwork/'})
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_unknown_material_no_next(self):
        response = self.client.get('/dashboard/editmaterials/999')
        self.assertRedirects(response, '/')

    def test_delete_material(self):
        # Create a work_type object
        materials.objects.create(name='test')
        # Get the category object
        material = materials.objects.first()
        response = self.client.get(f'/dashboard/editmaterials/{material.pk}')
        self.assertFalse(materials.objects.exists())

    def test_add_shipping(self):
        response = self.client.post(
            '/dashboard/addshipping/', {'region': 'test',
                                        'price': 50,
                                        'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)
        self.assertTrue(shipping.objects.exists())
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_shipping(self):
        # Create a shipping object
        shipping.objects.create(region='test', price=50)
        # Get the material object
        this_shipping = shipping.objects.first()
        response = self.client.post(
            f'/dashboard/editshipping/{this_shipping.pk}', {'region': 'testing',
                                                            'price': 51,
                                                            'next': '/dashboard/addwork/'})
        self.assertEqual(302, response.status_code)

    def test_edit_unknown_shipping(self):
        response = self.client.post(
            '/dashboard/editshipping/999', {'region': 'testing',
                                            'price': 51,
                                            'next': '/dashboard/addwork/'})
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_edit_unknown_shipping_no_next(self):
        response = self.client.get('/dashboard/editshipping/999')
        self.assertRedirects(response, '/')

    def test_delete_shipping(self):
        # Create a shipping object
        shipping.objects.create(region='test', price=50)
        # Get the shipping object
        this_shipping = shipping.objects.first()
        response = self.client.get(
            f'/dashboard/editshipping/{this_shipping.pk}')
        self.assertFalse(shipping.objects.exists())
