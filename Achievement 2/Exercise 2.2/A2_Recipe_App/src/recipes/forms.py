from django import forms

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120, required=False, label="Search by Recipe Name")
    chart_type = forms.ChoiceField(
        choices=[
            ('#1', 'Bar Chart - Cooking Time'),
            ('#2', 'Pie Chart - Difficulty'),
            ('#3', 'Line Chart - Trend')
        ],
        required=False,
        label="Select Chart Type"
    )