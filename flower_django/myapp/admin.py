from django.contrib import admin

# Register your models here.


from myapp.models import (
    Flower,
    Category,
    Tag
)


class FlowerAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": [
            "title",
        ]
    }

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": [
            "title",
        ]
    }



admin.site.register(Flower, FlowerAdmin)
admin.site.register(Category)
admin.site.register(Tag, TagAdmin)