from django.db import models


# def is_positive(value):
#     if value <= 0:
#         raise ValidationError


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'dog'),
        (TYPE_CHOICE_CAT, 'cat'),
        (TYPE_CHOICE_PARROT, 'parrot'),
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=6,
    )
    age = models.PositiveIntegerField(
        # validators=[
        #     # is_positive,
        # ]
    )
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f'{self.type} {self.name}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)