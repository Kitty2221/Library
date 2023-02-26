from django.urls import path
from api.user_api.views import users_list, users_detail, UserOrdersListView, OrderDetailView


urlpatterns = [
    path('user/', users_list, name="custom_users"),
    path('user/<int:pk>', users_detail, name="custom_user_by_id"),
    path('user/<user_id>/order/', UserOrdersListView.as_view()),
    path('user/<user_id>/order/<int:pk>', OrderDetailView.as_view()),

]
