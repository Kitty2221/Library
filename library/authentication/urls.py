from django.urls import path
import authentication.views as views


urlpatterns = [
    path("register/", views.register, name="register"),
    path('login/', views.login, name='login'),
    path("log_out/", views.log_out, name="log_out"),
    path("update/<int:user_id>/", views.edit_user, name="update"),
    path("", views.get_all, name="get_users"),
    path("delete/<int:id>/", views.delete_user, name="delete_user"),
    path("info/<int:id>/", views.user_info, name="user_info")

]
