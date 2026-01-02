from django.urls import path
from .views import home, recipes_list, recipes_detail

app_name = 'recipes'

urlpatterns = [
   path('', home, name='home'),
   path('list/', recipes_list, name='list'),
   path('list/<int:pk>/', recipes_detail, name='detail'),
]