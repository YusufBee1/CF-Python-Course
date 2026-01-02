from django.urls import path
from .views import home, recipes_list, recipes_detail, login_view, logout_view, about, RecipeCreateView

app_name = 'recipes'

urlpatterns = [
   path('', home, name='home'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path('list/', recipes_list, name='list'),
   path('list/<int:pk>/', recipes_detail, name='detail'),
   path('about/', about, name='about'),
   path('add/', RecipeCreateView.as_view(), name='add_recipe'),
]