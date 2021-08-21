from django.contrib import admin
from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age', 'likes_count')
    list_filter = ('name', )
    sortable_by = ('name', 'age', )

    @staticmethod
    def likes_count(obj):
        return obj.like_set.count()


admin.site.register(Pet, PetAdmin)
