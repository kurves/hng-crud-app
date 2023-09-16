from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
#from .views import PersonListView

#from crudapp.views import PersonsView

app_name="crudapp"
urlpatterns=[
    #home page
    path('', views.index, name='index'),
    path('api/',views.PersonListView.as_view(),name='Person-list'),
    path('api/<int:pk>',views.CreateUpdateView.as_view(),name='create-update'),
    path('api/<str:name>', views.PersonRetrieveByName.as_view(),name="Retrieve-Person-by-name")
   
]