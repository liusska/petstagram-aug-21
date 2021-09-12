from django.shortcuts import render, redirect
from petstagram.pets.models import Pet, Like
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from django.contrib.auth.decorators import login_required


def pet_list(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    is_owner = pet.user == request.user

    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }
        ),
        'comments': pet.comment_set.all(),
        'is_owner': is_owner,
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


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    liked_obj_by_user = pet.like_set.filter(user_id=request.user.id).first()
    if liked_obj_by_user:
        liked_obj_by_user.delete()
    else:
        like = Like(
            pet=pet,
            user=request.user,
        )
        like.save()
    return redirect('pet details', pet.id)


@login_required
def create_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
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
        form = EditPetForm(request.POST, request.FILES, instance=pet)
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
