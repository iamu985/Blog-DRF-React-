from django.urls import path
from .views import PostList, PostDetail

app_name = 'api'

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('detail/<slug:slug>', PostDetail.as_view(), name='postdetail'),
]
