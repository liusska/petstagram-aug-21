from django.urls import path
from petstagram.pets.views import pet_list, pet_details, pet_like


urlpatterns = [
    path('', pet_list, name="pet list"),
    path('details/<int:pk>', pet_details, name="pet details"),
    path('like/<int:pk>', pet_like, name="pet like"),
]