from django.test import TestCase
from .models import Resource, Meeting, Minutes
from django.urls import reverse

# Create your tests here.
#class ResourceTest(TestCase):
    # def test_stringOutput(self):
    #     resource=Resource(resourcename='laptop')
    #     self.assertEqual(str(resource), resource.resourcename)
    # def test_tablename(self):
    #     self.assertEqual(str(Resource._meta.db_table), 'resource')

class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')     
        