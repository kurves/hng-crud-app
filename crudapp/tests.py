from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
from .models import Person

class PersonAPITestCase(TestCase):
    ## Test for creating item
    def setup(self):
        self.client=APIClient()
        self.person_data={"name":"Mark Essien","details":"Software Engineer"}
        self.Person= Person.objects.create(**self.person_data)

    def test_create_person(self):
        self.person_data={"name":"Mark Essien","details":"Software Engineer"}
        response=self.client.post('/api/', self.person_data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_list_person(self):
        response = self.client.get('/api/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
          

    def test_update_person(self):
            updated_person={"name":"Maureen Mwenswa","details":"Civil engineer"}
            response=self.client.put('/api/<id>/', updated_person,format='json')
            self.assertEqual(updated_person["name"], "Maureen Mwenswa")
           


    def test_delete_person(self):
        response=self.client.delete('api/<int:pk>/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(Person.objects.filter(name="Mark Essien").exists()) 
        self.assertEqual(Person.objects.count(),0)


