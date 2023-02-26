from django.urls import path
from .views import *


urlpatterns = [
    path('book/', BookCreateView.as_view()),
    path('book', BookListView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view()),
]
