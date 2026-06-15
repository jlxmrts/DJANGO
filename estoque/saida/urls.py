from django.urls import path 
from .views import list_saida, new_saida, update_saida, delete_saida

app_name = 'saida' 
urlpatterns = [ 
    path('list_saida/', list_saida, name='list_saida'), 
    path('new_saida/', new_saida, name='new_saida'), 
    path('update_saida/<int:pk>/', update_saida, name='update_saida'), 
    path('delete_saida/<int:pk>/', delete_saida, name='delete_saida'), 
] 