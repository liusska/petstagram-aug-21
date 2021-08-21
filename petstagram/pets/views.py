from django.shortcuts import render, redirect
from petstagram.pets.models import Pet, Like


def pet_list(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet': pet,
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet
    )
    like.save()
    return pet_details(request, pk)
