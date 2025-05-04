from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='home'),
    path('blogs/',views.blogs_list,name='all_blogs')
]
