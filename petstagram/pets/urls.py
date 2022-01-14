from django.urls import path
from petstagram.pets.views import ListPetsView, PetDetailsView,\
    like_pet, CreatePet, EditPetView, delete_pet, CommentPetView

urlpatterns = [
    path('', ListPetsView.as_view(), name='list pets'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='details pets'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('create/', CreatePet.as_view(), name='create pet'),
    path('edit/<int:pk>', EditPetView.as_view(), name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('comment/<int:pk>', CommentPetView.as_view(), name='comment pet'),
]