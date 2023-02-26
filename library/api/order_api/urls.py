from django.urls import path
from .views import *


urlpatterns = [
    path('order/', OrderCreateView.as_view()),
    path('order', OrderListView.as_view()),
    path('order/<int:pk>', OrderDetailView.as_view()),
]

