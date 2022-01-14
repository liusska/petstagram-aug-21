from django.urls import path
from .views import LoginUserView, RegisterView, logout_user, ProfileDetailsView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),

]