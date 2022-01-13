from django.urls import path
from .views import login_user, RegisterView, logout_user, ProfileDetailsView

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),

]