from django.shortcuts import render
from categories.models import Categories
from categories.forms import Formulario_categories
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def list_categories(request):
    categories = Categories.objects.all() #Trae todos
    print(len(categories))
    context = {
        "categories" : categories
    }
    return render(request, "categories/categories_list.html", context=context)

def create_category(request): 
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            form = Formulario_categories(request.POST, request.FILES)

            if form.is_valid():
                Categories.objects.create(
                    name = form.cleaned_data["name"],
                    description = form.cleaned_data["description"],
                    image = form.cleaned_data["image"]
                )
                
                return redirect(list_categories)

        elif request.method == "GET":
            form =Formulario_categories()#initial={"name":"nombre"}
            context = {"form": form}
            return render(request, "categories/new_category.html", context=context)
    return redirect("login")
