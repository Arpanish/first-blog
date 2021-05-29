from django.urls import path
from.views import index, postlist, post_detail


urlpatterns = [
    path('', index, name='index'),
    path('post-list/', postlist, name='post-list'),
    path('post/detail/<int:id>/', post_detail, name='post_detail')
]
