from django.test import TestCase
from django.contrib.auth.models import User, Group
from works.models import work_items, categories, work_images
from shop.models import shop_items, work_types, work_sizes, materials
import base64               # for decoding base64 image
import tempfile             # for setting up tempdir for media
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class TestDashboardWorksViews(TestCase):

    def setUp(self):
        group = Group.objects.create(name='admin')
        user = User.objects.create_user(
            username='username', password='password')
        group.user_set.add(user)
        self.client.login(username='username', password='password')
        # Create a category object
        categories.objects.create(name='test')
        # Create a work type object
        work_types.objects.create(name='test')
        # Create a work size object
        work_sizes.objects.create(name='test')
        # Create a materials object
        materials.objects.create(name='test')

    def test_list_all_works(self):
        response = self.client.get('/dashboard/editworks/')
        self.assertTemplateUsed(response, 'listworks.html')

    def test_list_shop_works(self):
        response = self.client.get('/dashboard/listworks/shop')
        self.assertTemplateUsed(response, 'listworks.html')

    def test_list_works(self):
        response = self.client.get('/dashboard/listworks/work')
        self.assertTemplateUsed(response, 'listworks.html')

    def test_edit_unknown_work(self):
        response = self.client.get('/dashboard/editworks/1')
        self.assertRedirects(response, '/dashboard/addwork/')

    def test_add_work_item(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        response = self.client.post('/dashboard/addwork/', {'main_image': image,
                                                            'position': 'VT',
                                                            'category': category.pk,
                                                            'title': 'test',
                                                            'under_title': 'test',
                                                            'free_text': 'test',
                                                            'work_item': True,
                                                            'shop_item': True,
                                                            'collection': False,
                                                            'sort_order': 1},
                                    format='multipart/form-data')
        work = work_items.objects.first()
        self.assertEqual(302, response.status_code)
        self.assertTrue(work_items.objects.exists())
        self.assertRedirects(response, f'/dashboard/editworks/{work.pk}')

    def test_attach_shop_work(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        # Get the work type object
        work_type = work_types.objects.first()
        # Get the work size object
        work_size = work_sizes.objects.first()
        # Get the materials object
        material = materials.objects.first()
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image,
                                  shop_item=True)
        work = work_items.objects.first()
        response = self.client.post(f'/dashboard/editworks/{work.pk}', {'price': 50,
                                                                        'on_sale': True,
                                                                        'discount': 50,
                                                                        'stock': 50,
                                                                        'edition_count': 50,
                                                                        'work_type': work_type.pk,
                                                                        'material': material.pk,
                                                                        'work_size': work_size.pk,
                                                                        'frame': 'FR',
                                                                        'signed': True,
                                                                        'personal_message': 'test',
                                                                        'standard_text': True,
                                                                        'personal_text': False,
                                                                        'sort_order': 1})
        self.assertEqual(302, response.status_code)
        self.assertTrue(shop_items.objects.exists())
        self.assertRedirects(response, f'/dashboard/editworks/{work.pk}')

    def test_add_extra_image(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        extra_image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile2',
            name='tempfile2.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image)
        work = work_items.objects.first()
        response = self.client.post(f'/dashboard/editworks/{work.pk}', {'work_item': work.pk,
                                                                        'work_image': extra_image,
                                                                        'sort_order': 1},
                                    format='multipart/form-data')
        self.assertEqual(302, response.status_code)
        self.assertTrue(work_images.objects.exists())
        self.assertRedirects(response, f'/dashboard/editworks/{work.pk}')

    def test_delete_work(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        # Create a work object
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image,
                                  shop_item=True)
        work = work_items.objects.first()
        response = self.client.get(f'/dashboard/deletework/{work.pk}')
        self.assertTemplateUsed(response, 'delete_work.html')

    def test_delete_unknown_work(self):
        response = self.client.get(f'/dashboard/deletework/999')
        self.assertRedirects(response, '/dashboard/editworks/')

    def test_confirm_delete_work_and_its_extra_images(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        extra_image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile2',
            name='tempfile2.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        # Create a work object
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image,
                                  shop_item=True)
        work = work_items.objects.first()
        work_images.objects.create(work_item=work,
                                   work_image=extra_image,
                                   sort_order=1
                                   )
        response = self.client.post(f'/dashboard/deletework/{work.pk}')
        self.assertFalse(work_items.objects.exists())
        self.assertFalse(work_images.objects.exists())

    def test_delete_extra_images(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        extra_image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile2',
            name='tempfile2.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        # Create a work object
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image,
                                  shop_item=True)
        work = work_items.objects.first()
        work_images.objects.create(work_item=work,
                                   work_image=extra_image,
                                   sort_order=1
                                   )
        extra_image = work_images.objects.first()
        response = self.client.get(f'/dashboard/deleteimage/{extra_image.pk}')
        self.assertTemplateUsed(response, 'delete_image.html')

    def test_confirm_delete_extra_images(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        extra_image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile2',
            name='tempfile2.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        # Create a work object
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image,
                                  shop_item=True)
        work = work_items.objects.first()
        work_images.objects.create(work_item=work,
                                   work_image=extra_image,
                                   sort_order=1
                                   )
        extra_image = work_images.objects.first()
        response = self.client.post(f'/dashboard/deleteimage/{extra_image.pk}',
                                    {'next': '/dashboard/editworks/'})
        self.assertFalse(work_images.objects.exists())
        self.assertRedirects(response, '/dashboard/editworks/')

    def test_delete_unknown_extra_image(self):
        response = self.client.post('/dashboard/deleteimage/999',
                                    {'next': '/dashboard/editworks/'})
        self.assertRedirects(response, '/dashboard/editworks/')

    def test_set_works_order(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Get the category object
        category = categories.objects.first()
        # Create a work object
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image,
                                  shop_item=True)
        work = work_items.objects.first()
        response = self.client.post(f'/dashboard/worksorder/{work.pk}',
                                    {'sort_order': 3,
                                     'next': '/dashboard/editworks/'})
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, '/dashboard/editworks/')

    def test_set_unknown_works_order(self):
        response = self.client.post('/dashboard/worksorder/999',
                                    {'sort_order': 3,
                                     'next': '/dashboard/editworks/'})
        self.assertRedirects(response, '/dashboard/editworks/')


# Fake image data
TEST_IMAGE = '''
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
'''.strip()
