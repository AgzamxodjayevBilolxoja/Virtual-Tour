from django.urls import path

from users.views import register, user_login, change_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('change_user/', change_user, name='change_user'),
]