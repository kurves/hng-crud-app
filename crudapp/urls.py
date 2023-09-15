from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
#from .views import PersonListView

#from crudapp.views import PersonsView

app_name="crudapp"
urlpatterns=[
    #home page
    path('', views.index, name='index'),
    #path('api/', PersonsView.as_view(), name="PersonsVi2ew"),
    #path('api/', views.PersonListView.as_view(), name ='person-list'),
    #path('api/<str:name/',views.PersonRetrieveUpdate.as_view(),name='detail'),
    #path('api/', views.new_person, name='new_person'),
    #path('api/<person_id>',views.update_person, name='update_person'),
    #path('api/<str:name>', views.search_person, name='search_person'),
    #path('api/person', views.person, name='person') ,
    #path('api/<person_id>',views.update_person, name='update_person'),
    #path('api/<person_id>/', views.delete_person, name='delete_person'),
    #path('api/<person_id>', views.person, name='person'),
    #path('api/<int:pk>/',csrf_exempt(views.PatchModelView.as_view()),name='person-patch'),
    #path('api/<int:pk>/', views.PersonDeleteView.as_view(),name='person-delete')
    #path('api/<int:pk>/',csrf_exempt(views.PatchModelView.as_view()),name='person-patch'),
    path('api/',views.PersonListView.as_view(),name='Person-list'),
    path('api/<int:pk>/',views.CreateUpdateView.as_view(),name='create-update'),
    path('api/<str:name>/', views.PersonRetrieveByName.as_view(),name="Retrieve-Person-by-name")
   
]