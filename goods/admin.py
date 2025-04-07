from django.contrib import admin


from goods.models import Categories, Products


#admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Categories)
class Categories_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display = ["name",]

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount",]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category", "type_of_personality"]
    fields = [
        "name",
        "category",
        "type_of_personality",
        "slug",
        "description",
        "type_product",
        "pyramid_of_fragrance",
        "product_weight",
        "image",
        ("price", "discount"),
        "quantity",

    ]