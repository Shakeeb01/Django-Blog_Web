from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='home'),
    path('blogs/',views.blogs_list,name='all_blogs'),
    path('create-blog/',views.post_create_update_view,name='create_blog'),
    path('update-blog/<int:pk>',views.post_create_update_view,name='update_blog'),
    path('delete-blog/<int:pk>',views.delete_blog,name='delete_blog')
]
