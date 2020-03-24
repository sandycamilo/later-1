from django.urls import path, include
from .views import (
    BooksListView,
    BooksDetailView,
    BooksCreateView,
    BooksUpdateView,
    BooksDeleteView
)

from . import views

# from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static
# from usersApp import views as user_views

urlpatterns = [
    path('', BooksListView.as_view(), name='book-home'),
    path('listApp/<int:pk>/', BooksDetailView.as_view(), name='book-detail'),
    path('listApp/new/', BooksCreateView.as_view(), name='book-create'),
    path('listApp/<int:pk>/update', BooksUpdateView.as_view(), name='book-update'),
    path('listApp/<int:pk>/delete', BooksDeleteView.as_view(), name='book-delete'),

    # path('register/', user_views.register, name="register"),
    # path('profile/', user_views.profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(template_name="usersApp/login.html"), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(template_name="usersApp/logout.html"), name="logout"),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name="usersApp/password_reset.html"), name="password_reset"),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="usersApp/password_reset_done.html"), name="password_reset_done"),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="usersApp/password_reset_confirm.html"), name="password_reset_confirm"),
    # path('', include('listApp.urls')),
]
