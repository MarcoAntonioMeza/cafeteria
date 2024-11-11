# views.py
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user/index.html'
    # Redirige a la página de inicio de sesión si no está autenticado
    login_url = 'login'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user/form_.html'
    success_url = reverse_lazy('user_list')
    login_url = 'login'

class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user/view.html'
    context_object_name = 'user'
    login_url = 'login'

class UserUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'user/view.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
