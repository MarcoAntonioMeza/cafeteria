# urls.py
from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from .views import UserCreateView, UserUpdateView, UserDeleteView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('nuevo/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/editar/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/eliminar/', UserDeleteView.as_view(), name='user_delete'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
