from django.urls import path
from users.views import login_request, register, perfil, editar_perfil, ChangePasswordView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name = "users/logout.html"), name="logout"),
    path("profile/", perfil, name="profile"),
    path("update-usuario/", editar_perfil, name="update_user"),
    path("cambiar-contraseña/", ChangePasswordView.as_view(), name="cambiar_password"),
]