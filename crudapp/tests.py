from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Person

class PersonCrudTests(TestCase):
    ## Test for creating item
    def setup(self):
        self.Person.objects.create(name = "Mark Essien",details='Software Engineer')

    def test_new_person_view(self):
        res= self.client.post(reverse("crudapp:new_person"),{'name':"Mark Essien","details":"Software Engineer"})
        self.assertEqual(res.status_code,302)
        self.assertTrue(Person.objects.filter(name='Mark Essien').exists())


    def test_person_view(self):
        res=self.client.get(reverse("crudapp:search_person",args=[id])) 
        self.assertEqual(res.status_code, 200)
        #self.assertContains(res,"Mark Essien")

    def test_delete_person_view(self):
        res=self.client.post(reverse('crudapp:update_person',args=[id]))
        self.assertEqual(res.status_code,200)
        self.assertFalse(Person.objects.filter(name="Mark Essien").exists())  

    def test_update_person_view(self):
        res=self.client.post(reverse('crudapp:new_person'),{'name':'new person','details':'This is a new person'})    
        self.assertEqual(res.status_code,302)
        updated_name=Person.objects.get()
        self.assertNotEqual(updated_name, 'new person' )   