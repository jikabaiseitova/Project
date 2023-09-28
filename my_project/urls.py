from django.urls import path

from . import views
from .views import index, book, detail, update, delete


urlpatterns = [
    path('', index),
    path('book/', book),
    path('book/search/', views.search, name='search'),
    path('book/<int:book_id>/', detail, name='detail'),
    path('book/<int:book_id>/update', update, name='update'),
    path('book/<int:book_id>/delete', delete, name='delete'),

]
