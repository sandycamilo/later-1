from django.urls import path, include
from .views import (
    HomePageView,
    HomeView,
    BooksListView,
    BooksDetailView,
    MusicListView,
    BooksCreateView,
    BooksUpdateView,
    BooksDeleteView
)

from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('home/', HomeView.as_view(), name='home'),
    # path('user/<str:username>', UserListView.as_view(), name='user-lists'),
    path('listApp/<int:pk>/', BooksDetailView.as_view(), name='book-detail'),
    path('listApp/new/', BooksCreateView.as_view(), name='book-create'),
    path('listApp/booklist/',BooksListView.as_view(), name='book-list'),
    path('listApp/musiclist/',MusicListView.as_view(), name='music-list'),
    path('listApp/<int:pk>/update', BooksUpdateView.as_view(), name='book-update'),
    path('listApp/<int:pk>/delete', BooksDeleteView.as_view(), name='book-delete'),
    path('listApp/music/', views.music_api_view, name='music'),
    path('listApp/books/', views.book_api_view, name='books'),
]
