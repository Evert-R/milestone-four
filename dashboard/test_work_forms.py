from django.test import TestCase
from .forms import EditWorksForm, AddExtraImagesForm, EditShopWorksForm
from works.models import work_items, categories, work_images
from shop.models import shop_items, work_sizes, work_types, materials
import base64               # for decoding base64 image
import tempfile             # for setting up tempdir for media
from io import BytesIO
from django.test import TestCase
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your tests here.
# self.assertEqual(form.errors, '6767')


class TestEditShopWorksForm(TestCase):

    def setUp(self):
        # Create a work type object
        work_types.objects.create(name='test')
        # Create a work size object
        work_sizes.objects.create(name='test')
        # Create a materials object
        materials.objects.create(name='test')

    def test_create_shop_work_all_fields(self):
        # Get the work type object
        work_type = work_types.objects.first()
        # Get the work size object
        work_size = work_sizes.objects.first()
        # Get the materials object
        material = materials.objects.first()

        form = EditShopWorksForm({'price': 50,
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
        self.assertTrue(form.is_valid())

    def test_create_shop_work_no_required_fields(self):
        # Get the work type object
        work_type = work_types.objects.first()
        # Get the work size object
        work_size = work_sizes.objects.first()
        # Get the materials object
        material = materials.objects.first()

        form = EditShopWorksForm({'price': '',
                                  'on_sale': True,
                                  'discount': '',
                                  'stock': '',
                                  'edition_count': '',
                                  'work_type': '',
                                  'material': '',
                                  'work_size': '',
                                  'frame': 'FR',
                                  'signed': True,
                                  'personal_message': 'test',
                                  'standard_text': True,
                                  'personal_text': False,
                                  'sort_order': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertIn('discount', form.errors.keys())
        self.assertIn('stock', form.errors.keys())
        self.assertIn('edition_count', form.errors.keys())
        self.assertIn('work_type', form.errors.keys())
        self.assertIn('material', form.errors.keys())
        self.assertIn('work_size', form.errors.keys())
        self.assertIn('sort_order', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')
        self.assertEqual(form.errors['discount'][0], 'This field is required.')
        self.assertEqual(form.errors['stock'][0], 'This field is required.')
        self.assertEqual(form.errors['edition_count']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['work_type']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['material'][0], 'This field is required.')
        self.assertEqual(form.errors['work_size']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['sort_order']
                         [0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test if only fields in the Meta class are displayed
        """
        form = EditShopWorksForm()
        self.assertEqual(form.Meta.fields, ['price', 'on_sale', 'discount',
                                            'stock', 'edition_count', 'work_type',
                                            'material', 'work_size', 'frame',
                                            'signed', 'personal_message', 'standard_text',
                                            'personal_text', 'sort_order'])


class TestEditWorksForm(TestCase):

    def setUp(self):
        # Create a category object
        categories.objects.create(name='test')

    def test_create_work_all_fields(self):
        # Get the category object
        category = categories.objects.first()
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        form = EditWorksForm({'position': 'VT',
                              'category': category.pk,
                              'title': 'test',
                              'under_title': 'test',
                              'free_text': 'test',
                              'work_item': True,
                              'shop_item': True,
                              'collection': False,
                              'sort_order': 1},
                             files={'main_image': image})
        self.assertTrue(form.is_valid())

    def test_create_work_no_required_fields(self):
        # Get the category object
        category = categories.objects.first()
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        form = EditWorksForm({'position': '',
                              'category': '',
                              'title': '',
                              'under_title': 'test',
                              'free_text': 'test',
                              'work_item': True,
                              'shop_item': True,
                              'collection': False,
                              'sort_order': 1},
                             files={'main_image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('position', form.errors.keys())
        self.assertIn('category', form.errors.keys())
        self.assertIn('title', form.errors.keys())
        self.assertIn('main_image', form.errors.keys())
        self.assertEqual(form.errors['position'][0], 'This field is required.')
        self.assertEqual(form.errors['category'][0], 'This field is required.')
        self.assertEqual(form.errors['title'][0], 'This field is required.')
        self.assertEqual(form.errors['main_image']
                         [0], 'This field is required.')

    def test_create_work_required_fields(self):
        # Get the category object
        category = categories.objects.first()
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        form = EditWorksForm({'position': 'VT',
                              'category': category.pk,
                              'title': 'test',
                              'sort_order': 1},
                             files={'main_image': image})
        self.assertTrue(form.is_valid())

    def test_create_work_only_title(self):
        form = EditWorksForm({'title': 'This test'})
        self.assertFalse(form.is_valid())

    def test_create_work_only_image(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        form = EditWorksForm({}, files={'main_image': image})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test if only fields in the Meta class are displayed
        """
        form = EditWorksForm()
        self.assertEqual(form.Meta.fields, ['main_image', 'position', 'category', 'title',
                                            'under_title', 'free_text', 'work_item',
                                            'shop_item', 'collection', 'sort_order'])


class TestAddExtraImagesForm(TestCase):

    def setUp(self):
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        # Create a category object
        categories.objects.create(name='test')
        # Get the category object
        category = categories.objects.first()
        # Create a work object
        work_items.objects.create(position='VT',
                                  category=category,
                                  title='test',
                                  main_image=image)

    def test_add_extra_images_all_fields(self):
         # Get the category object
        work = work_items.objects.first()
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )

        form = AddExtraImagesForm({
            'work_item': work.pk,
            'sort_order': 1},
            files={'work_image': image})
        self.assertTrue(form.is_valid())

    def test_add_extra_images_no_required_fields(self):
         # Get the category object
        work = work_items.objects.first()
        # Create a fake image
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )

        form = AddExtraImagesForm({
            'work_item': '',
            'sort_order': 1},
            files={'work_image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('work_item', form.errors.keys())
        self.assertIn('work_image', form.errors.keys())
        self.assertEqual(form.errors['work_item']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['work_image']
                         [0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test if only fields in the Meta class are displayed
        """
        form = AddExtraImagesForm()
        self.assertEqual(form.Meta.fields, ['work_item', 'work_image'])


# Fake image data
TEST_IMAGE = '''
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
'''.strip()
