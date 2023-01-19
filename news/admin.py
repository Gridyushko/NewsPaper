from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment



class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category__name')


class PostAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category__name')



admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)

