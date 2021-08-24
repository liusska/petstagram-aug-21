from django.shortcuts import render, redirect
from petstagram.pets.models import Pet, Like
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment


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
        'comment_form': CommentForm(
            # variant 2
            # initial={
            #     'pet_pk': pk,
            # }
        ),
        'comments': pet.comment_set.all(),
    }
    return render(request, 'pets/pet_detail.html', context)


def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            text=form.cleaned_data['text'],
            pet=pet,
        )
        comment.save()

    return redirect('pet details', pet.id)

# variant 2
#
# def comment_pet(request, pk):
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment.save()
#
#     return redirect('pet details', pk)


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet
    )
    like.save()
    return pet_details(request, pk)


def create_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet list')
    else:
        form = PetForm()
    context = {
        'form': form,
    }
    return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet list')
    else:
        form = EditPetForm(instance=pet)
    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'pets/pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        pet.delete()
        return redirect('pet list')
    context = {
        'pet': pet,
    }
    return render(request, 'pets/pet_delete.html', context)
