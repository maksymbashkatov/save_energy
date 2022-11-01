from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from users.forms import CustomUserCreationForm
from users.models import CustomUser


class UserListView(ListView):
    queryset = CustomUser.objects.all()
    template_name = 'users/users_list.html'


class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'reg_auth/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLoginView(LoginView):
    next_page = reverse_lazy('users_list')
    template_name = 'reg_auth/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
