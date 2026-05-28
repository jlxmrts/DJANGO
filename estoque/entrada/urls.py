from django.urls import path 
from .views import list_entrada, new_entrada, update_entrada, delete_entrada 

app_name = 'entrada' 
urlpatterns = [ 
    path('list_entrada/', list_entrada, name='list_entrada'), 
    path('new_entrada/', new_entrada, name='new_entrada'), 
    path('update_entrada/<int:pk>/', update_entrada, name='update_entrada'), 
    path('delete_entrada/<int:pk>/', delete_entrada, name='delete_entrada'), 
] 