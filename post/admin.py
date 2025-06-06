from django.contrib import admin
from .models import Category,Post




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','body','category','posted']