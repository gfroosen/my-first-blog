from django.contrib import admin
from .models import Post
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display=['title','amount']



admin.site.register(Post)
admin.site.register(Item,ItemAdmin)

# Register your models here.
