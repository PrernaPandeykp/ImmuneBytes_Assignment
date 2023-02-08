from django.urls import path
from . import views
from .views import LoginView, CreateAccountView, RemoveAccountView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', CreateAccountView.as_view(), name='register'),
    path('remove_account/', RemoveAccountView.as_view(), name='remove_account'),
    # path('login/', views.login, name='login'),
    # path('register/', views.create_account, name='register'),
    # ... other API URL patterns ...
]
