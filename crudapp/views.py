from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.views.generic import View
from .models import Person
from .forms import PersonForm
# Create your views here.

def  index(request):
    return render(request,'crudapp/index.html')

def person(request,name):
    try:
        person=Person.objects.get(pk=name)
        context={'person':person}
        return render(request, 'crudapp/person.html',context)
    except (ValueError,Person.DoesNotExist):
        pass

    results=Person.objects.filter(name__icontains=name)

    context={'results':results,'name':name}    
    return render(request,'crudapp/search.html',context)       

def new_person(request):
    
    persons=Person.objects.all()
    context={'persons': persons}
    #return render(request, 'crudapp/persons.html' ,context)

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("crudapp:new_person"))
    else:
        form = PersonForm() 
    context={'form': form,'persons':persons}
    return render(request,'crudapp/new_person.html', context)



def update_person(request,person_id):
    person=Person.objects.get(id=person_id)
    if request.method =='POST':
        form= PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("crudapp:new_person"))
    else:
        form=PersonForm(instance=person)
    context={'form':form,'person':person}    
    return render(request, 'crudapp/update_person.html',context)       


def delete_person(request,person_id):
    person=Person.objects.get(id=person_id)
    if request.method =='POST':
        person.delete()
        return HttpResponseRedirect(reverse("crudapp:new_person"))
     
    context= {'person':person}   
    return render(request, 'crudapp/delete_person.html',context)    


"""def search_person(request,name):
    try:
        person=Person.objects.get(pk=name)
        context={'person':person}
        return render(request, 'crudapp/person.html',context)
    except (ValueError,Person.DoesNotExist):
        pass

    results=Person.objects.filter(name__icontains=name)
    
    context={'results':results,'name':name}    
    return render(request,'crudapp/search.html',context)  """     




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
    
    context={'results':results,'name':name}    
    return render(request,'crudapp/search.html',context)     







"""def update_person(request,person_id):
    person=Person.objects.get(id=person_id)
    if request.method =='POST':
        form= PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("crudapp:new_person"))
    else:
        form=PersonForm(instance=person)
    context={'form':form,'person':person}    
    return render(request, 'crudapp/update_person.html',context)    """