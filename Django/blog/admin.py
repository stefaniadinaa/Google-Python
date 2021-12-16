from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('data_created', 'author')

admin.site.register(Post)
