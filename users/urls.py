from django.urls import path
from users.views import RegisterFormView, CustomLoginView, CustomLogoutView, UserListView

urlpatterns = (
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('all', UserListView.as_view(), name='users_list')
)
