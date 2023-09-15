from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.urls import reverse
from django.http import JsonResponse
#from django.views.generic import View
from .models import Person
from .forms import PersonForm
# Create your views here.
from rest_framework import generics, status
from .serializers import PersonSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

def  index(request):
    return render(request,'index.html')
   
class PersonListView(generics.ListCreateAPIView):
    queryset =Person.objects.all()
    serializer_class =PersonSerializer

class CreateUpdateView(generics.UpdateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class= PersonSerializer    

class PersonRetrieveByName(generics.RetrieveAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer    
    lookup_field="name"
    
    def list(self,request,*args,**kwargs):
        name=self.kwargs['name']
        queryset=self.get_queryset().filter(name=name)
        serializer= PersonSerializer(queryset,many=True)
        return Response(serializer.data)