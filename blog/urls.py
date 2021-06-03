from django.urls import path
from.views import index, PostList, post_detail, Login, signup, AddPost, deletepost, EditPost


urlpatterns = [
    path('', index, name='index'),
    path('post-list/', PostList.as_view(), name='post-list'),
    path('post/detail/<int:id>/', post_detail, name='post_detail'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', signup.as_view(), name='signup'),
    path('add-post/', AddPost.as_view(), name='add-post'),
    path('delete-post/<int:id>/', deletepost, name='delete-post'),
    path('edit-post/<int:id>/', EditPost.as_view(), name='edit-post'),
]


