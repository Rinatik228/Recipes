from django.shortcuts import render
from recipe.data import recipes
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def recipe_list(request):
    category_rec = {
        "Завтрак": [],
        "Обед": [],
        "Ужин": [],
        "Перекус": []
    }
    for i in recipes:
        category = i['recipe']['category']
        if category in category_rec:
            category_rec[category].append(i)
            
    return render(request, 'recipe_list.html', context=category_rec)

def recipe_id(request, id):
    try:
        recipe = recipes[id-1]
        return render(request, 'recipe_detail.html', context={'recipe': recipe})
    except IndexError:
        return HttpResponse("Рецепт с таким индексом не найден", status=404)
