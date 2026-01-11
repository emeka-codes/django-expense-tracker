from django.urls import path
from . import views

urlpatterns= [
    path('home', views.display_home),
    path('delete_expense', views.delete_expense, name='delete_expense'),
    path('edit_expense_modal', views.edit_expense, name='edit_expense_modal'),
    path('search_by_date', views.search_by_date, name='search_by_date'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('signup', views.user_signup, name='user_signup'),
]