from django.urls import path
from .views import login_user, RegisterView, logout_user, profile_details

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_details, name='profile details'),

]