from django.test import TestCase
from nippo.models import NippoModel

class NippoTestCase(TestCase):
    def setUp(self):
        obj = NippoModel(title="testTitle1", content="testContent1")
        obj.save()

#データベースに保存されるか確認
    def test_saved_single_object(self):
        qs_counter = NippoModel.objects.count()
        self.assertEqual(qs_counter, 1)