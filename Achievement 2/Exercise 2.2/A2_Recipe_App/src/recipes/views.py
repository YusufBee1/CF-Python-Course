from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Recipe

# HOME PAGE (Public)
def home(request):
   return render(request, 'recipes/recipes_home.html')

# LOGIN VIEW
def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipes:list')  # Redirect to the recipe list after login
        else:
            error_message = 'Invalid username or password'
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form, 
        'error_message': error_message
    }
    return render(request, 'recipes/login.html', context)

# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return render(request, 'recipes/success.html')

# RECIPE LIST (Protected)
@login_required
def recipes_list(request):
   recipes = Recipe.objects.all()
   return render(request, 'recipes/recipes_list.html', {'recipes': recipes})

# RECIPE DETAIL (Protected)
@login_required
def recipes_detail(request, pk):
   recipe = Recipe.objects.get(pk=pk)
   # Python-side split for ingredients
   ingredients_list = recipe.ingredients.split(',')
   return render(request, 'recipes/recipes_detail.html', {
       'recipe': recipe,
       'ingredients_list': ingredients_list
   })