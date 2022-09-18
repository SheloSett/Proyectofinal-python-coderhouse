from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from proyectofinal.views import index
from users.models import User_profile
from users.forms import User_registration_form, User_profile_form
from django.views.generic import  DetailView
from django.http import HttpResponse


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)

                context = {"message": f"Bienvenido {username} !! :D"}
                return render(request, "index.html", context=context)

        form = AuthenticationForm()
        return render(request, "users/login.html", {"error": "Formulario invalido","form":form})
    
    elif request.method == "GET":
        form = AuthenticationForm()
    return render(request, "users/login.html", { "form":form})

def register(request):
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context = {"errors":form.errors}
            form = User_registration_form
            context["form"] = form
            return render(request, "users/register.html", context)

    elif request.method == "GET":
        form = User_registration_form
        return render(request, "users/register.html", {"form":form})
        
""" def show_profile(request, pk):
    if request.method == "GET":
        perfil = User_profile.objects.get(user_id=pk)
        
        form = User_profile_form(initial={
                                        "user":perfil.user,
                                        "phone":perfil.phone,
                                        "address":perfil.address,
                                        "image":perfil.image
                                        })
        context = {"form" : form}
    
    return render(request, "users/show_profile.html", context=context)

class ShowProfile(DetailView):
    model = User_profile
    template_name = "users/show_profile.html"

def update_user(request):
    user = request.user
    user_profile = User_profile.objects.get_or_create(user=user)
    if request.method == "POST":
        form = User_profile_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data.get("user"):
                user.user = data.get("user")
            if data.get("phone"):
                user.phone = data.get("phone")
            if data.get("address"):
                user.address = data.get("address")
            if data.get("image"):
                user_profile.image = data.get("image")
            user_profile.save()
            user.save()

            return redirect(index)
        else:
            return render(request, "users/update_user.html", {"form":form})
    
    form = User_profile_form(
        initial={
            "username":user.username,
            "phone":user.phone,
            "address":user.address,
            "image":user_profile.image
            }
        )
    return render(request, "users/update_user.html", {"form":form}) """

@login_required
def perfil(request):
    return render(request, 'users/show_profile.html')

@login_required
def editar_perfil(request):

    user = request.user
    mas_datos_usuario, _ = User_profile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = User_profile_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            if data.get('username'):
                user.username = data.get('username')
 
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuario.phone = data.get('phone') if data.get('phone') else mas_datos_usuario.phone
            mas_datos_usuario.address = data.get('address') if data.get('address') else mas_datos_usuario.phone
            mas_datos_usuario.image = data.get('image') if data.get('image') else mas_datos_usuario.image
            
            # if data.get('password1') and data.get('password1') == data.get('password2'):
            #     user.set_password(data.get('password1'))
            
            mas_datos_usuario.save()
            user.save()
    
            return redirect('index')
        
        else:
            return render(request, 'users/update_user.html', {'form': form})
            
    form = User_profile_form(
            initial={
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone': mas_datos_usuario.phone,
                'address': mas_datos_usuario.address,
                'image': mas_datos_usuario.image
            }
        )

    return render(request, 'users/update_user.html', {'form': form})

class ChangePasswordView(PasswordChangeView):
    template_name = 'users/cambio_password.html'
    success_url = "/users/profile/"


