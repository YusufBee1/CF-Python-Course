from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipesSearchForm
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64

# --- UTILITY: GET CHART ---
def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG') # Prevent GUI errors
    fig = plt.figure(figsize=(6, 3))
    
    if chart_type == '#1': # Bar Chart
        plt.bar(data['name'], data['cooking_time'])
        plt.title('Cooking Time per Recipe')
        plt.xlabel('Recipe Name')
        plt.ylabel('Minutes')
    elif chart_type == '#2': # Pie Chart
        labels = kwargs.get('labels')
        plt.pie(data['count'], labels=labels, autopct='%1.1f%%')
        plt.title('Difficulty Distribution')
    elif chart_type == '#3': # Line Chart
        plt.plot(data['name'], data['cooking_time'])
        plt.title('Cooking Time Trend')
        plt.xlabel('Recipe')
        plt.ylabel('Minutes')
    else:
        print('Unknown chart type')

    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# --- VIEWS ---

def home(request):
    return render(request, 'recipes/recipes_home.html')

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipes:list')
        else:
            error_message = 'Invalid username or password'
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form, 'error_message': error_message})

def logout_view(request):
    logout(request)
    return render(request, 'recipes/success.html')

@login_required
def recipes_list(request):
    form = RecipesSearchForm(request.POST or None)
    recipes_df = None
    chart = None

    # Default: Show all
    qs = Recipe.objects.all()

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        chart_type = request.POST.get('chart_type')

        # Filter by name if provided
        if recipe_name:
            qs = qs.filter(name__icontains=recipe_name)

        # Create DataFrame if data exists
        if qs.exists():
            recipes_df = pd.DataFrame(qs.values())
            
            # Make the ID clickable (we'll fix the link in template, but prep data here)
            # Generate Chart
            if chart_type:
                if chart_type == '#1':
                    chart = get_chart(chart_type, recipes_df)
                elif chart_type == '#2':
                    # Group for Pie Chart
                    data = recipes_df['difficulty'].value_counts().reset_index()
                    data.columns = ['difficulty', 'count']
                    chart = get_chart(chart_type, data, labels=data['difficulty'])
                elif chart_type == '#3':
                    chart = get_chart(chart_type, recipes_df)
                    
            # Convert DF to HTML for display
            recipes_df = recipes_df.to_html(classes='table table-striped', index=False, escape=False)

    return render(request, 'recipes/recipes_search.html', {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart
    })

@login_required
def recipes_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients_list = recipe.ingredients.split(',')
    return render(request, 'recipes/recipes_detail.html', {
        'recipe': recipe,
        'ingredients_list': ingredients_list
    })