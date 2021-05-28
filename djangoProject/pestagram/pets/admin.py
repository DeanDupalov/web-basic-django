from django.contrib import admin

from pets.models import Pet, Like


# class LikeInline(admin.TabularInline):
#     model = Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'age')
    list_filter = ('type',)
    # inlines = (
    #     LikeInline,
    # )


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
