from django.urls import path 
from .views import list_saida, new_saida, update_saida, delete_saida

app_name = 'saida' 
urlpatterns = [ 
    path('list_saida/', list_saida, name='list_saida'), 
    path('new_entrada/', new_entrada, name='new_entrada'), 
    path('update_entrada/<int:pk>/', update_entrada, name='update_entrada'), 
    path('delete_entrada/<int:pk>/', delete_entrada, name='delete_entrada'), 
] 