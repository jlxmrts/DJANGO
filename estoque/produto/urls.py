from django.urls import path 
from .views import list_produto, new_produto, update_produto, delete_produto 

app_name = 'produto' 

urlpatterns = [ 
    path('list_produto/', list_produto, name='list_produto'), 
    path('new_produto/', new_produto, name='new_produto'), 
    path('update_produto/<int:pk>/', update_produto, name='update_produto'), 
    path('delete_produto/<int:pk>/', delete_produto, name='delete_produto'), 
] 