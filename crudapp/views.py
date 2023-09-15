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
    return render(request,'crudapp/index.html')
   
"""@csrf_exempt
def new_person(request):
    
    persons=Person.objects.all()
    context={'persons': persons}
    #return render(request, 'crudapp/persons.html' ,context)

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse()
            return HttpResponseRedirect(reverse("crudapp:new_person"))
            
    else:
        form = PersonForm() 
    context={'form': form,'persons':persons}
    return render(request,'crudapp/new_person.html', context)  


def delete_person(request,person_id):
    person=Person.objects.get(id=person_id)
    if request.method =='POST':
        person.delete()
        return HttpResponseRedirect(reverse("crudapp:new_person"))
     
    context= {'person':person}   
    return render(request, 'crudapp/delete_person.html',context)    
 


def search_person(request,name):
    try:
        person=Person.objects.get(pk=name)

        if request.method =='POST':
                form= PersonForm(request.POST, instance=person)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse("crudapp:new_person"))
        else:
                
                form=PersonForm(instance=person)
        context={'form':form,'person':person}    
        return render(request, 'crudapp/update_person.html',context) 




        context={'person':person}
        return render(request, 'crudapp/person.html',context)
    except (ValueError,Person.DoesNotExist):
        pass

    results=Person.objects.filter(name__icontains=name)
    #serializer=PersonSerializer(results)
   # return JsonResponse(serializer.data)
    context={'results':results,'name':name}    
    return render(request,'crudapp/search.html',context)     """


class PersonListView(generics.ListCreateAPIView):
    queryset =Person.objects.all()
    serializer_class =PersonSerializer

class CreateUpdateView(generics.UpdateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class= PersonSerializer    

class PersonRetrieveByName(generics.RetrieveAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView,generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer    
    lookup_field="name"
    
    def list(self,request,*args,**kwargs):
        name=self.kwargs['name']
        queryset=self.get_queryset().filter(name=name)
        serializer= PersonSerializer(queryset,many=True)
        return Response(serializer.data)