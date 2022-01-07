from django.urls import path
from .views import login_user, register_user, logout_user, profile_details

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', profile_details, name='profile details'),

]