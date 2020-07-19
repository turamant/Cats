from django.contrib import admin

# Register your models here.
from posts.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'image')
    search_fields = ('title',)
    prepopulated_fields = {'url':('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title',)
    prepopulated_fields = {'url':('title',)}
