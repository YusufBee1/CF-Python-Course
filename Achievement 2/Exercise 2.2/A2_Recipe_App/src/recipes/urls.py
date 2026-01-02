from django.urls import path
from .views import home, recipes_list, recipes_detail, login_view, logout_view

app_name = 'recipes'

urlpatterns = [
   path('', home, name='home'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path('list/', recipes_list, name='list'), # This now points to the search view
   path('list/<int:pk>/', recipes_detail, name='detail'),
]