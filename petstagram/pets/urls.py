from django.urls import path
from petstagram.pets.views import pet_list, pet_details, pet_like
from petstagram.pets.views import create_pet, edit_pet, delete_pet, comment_pet


urlpatterns = [
    path('', pet_list, name='pet list'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', pet_like, name='pet like'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('comment/<int:pk>', comment_pet, name='comment pet'),
]