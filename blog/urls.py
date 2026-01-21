from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('detail_blog/<int:pk>',detail_blog,name='detail_blog'),
    path('edit_blog/<int:pk>',edit_blog,name='edit_blog'),
    path('delete_blog/<int:pk>',delete_blog,name='delete_blog'),
    path('create_post',create_post,name='create_post'),
    path('tags/<slug:tag_slug>',get_tags,name='get_tags'),
    path('comment',save_comment,name='comment'),
    path('delete', delete_comment,name='delete'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
]
