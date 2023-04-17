from django.test import TestCase
from ..models.models import Animal

# Create your tests here.
class AnimalTestCase(TestCase):
    def setUp(self):
        # print("hello")
        Animal.objects.create(name="lion",sound="roar")
        Animal.objects.create(name="cat",sound="meow")

    def test_animal_speak(self): # test case method have to begin with "test"
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        print(lion)
        self.assertEqual(lion.speak(),"lion speaks roar")
        self.assertEqual(cat.speak(),"cat speaks meow")