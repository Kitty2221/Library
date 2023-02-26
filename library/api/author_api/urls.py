from django.urls import path
from .views import *


urlpatterns = [
    path('author/', AuthorCreateView.as_view()),
    path('author', AuthorListView.as_view()),
    path('author/<int:pk>', AuthorDetailView.as_view()),
]
