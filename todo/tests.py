from django.test import TestCase, Client
from todo.models import car_info

# Create your tests here.

class PageTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        car_info.objects.create(brand="new", consommation=7)
    def test_liste(self):
        
        #Get to the page list
        response = self.c.get("/liste/")
        self.assertEqual(response.status_code, 200)
    def test_delete(self):
        
        #When the object with pk=1 (created in setUp) is deleted
        response = self.c.post("/delete/1/")
        self.assertEqual(car_info.objects.count(), 0)
    def test_add(self):

        #When a new object is added
        response = self.c.post("/add/", {'brand': "new2", "consommation":8})
        self.assertEqual(car_info.objects.count(), 2)
    

