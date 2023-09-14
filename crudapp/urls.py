from django.urls import path
from . import views
#from crudapp.views import PersonsView

app_name="crudapp"
urlpatterns=[
    #home page
    path('', views.index, name='index'),
    #path('api/', PersonsView.as_view(), name="PersonsView"),

    path('api/', views.new_person, name='new_person'),
    #path('api/<person_id>',views.update_person, name='update_person'),
    path('api/<str:name>', views.search_person, name='search_person'),
    #path('api/person', views.person, name='person') ,
    path('api/<person_id>',views.update_person, name='update_person'),
    path('api/<person_id>/', views.delete_person, name='delete_person'),
    path('api/<person_id>', views.person, name='person'),
   
   
]