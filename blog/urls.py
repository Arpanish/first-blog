from django.urls import path
from.views import index, postlist


urlpatterns = [
    path('', index, name='index'),
    path('post-list/', postlist, name='post-list')
]