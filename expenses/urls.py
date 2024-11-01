from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list_expenses, name='list_expenses'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="expenses/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
