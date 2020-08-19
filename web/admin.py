from django.contrib import admin
from .models import  Category, Movie



class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster', 'genres', 'category', 'url', 'draf')
    list_filter = ('title', 'poster', 'category', 'genres', 'draf' )
    search_fields = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'url')
    list_filter = ('name', 'description', 'image', 'url')
    search_fields = ('name', 'description')

admin.site.register(Movie,MovieAdmin )
admin.site.register(Category,CategoryAdmin)



