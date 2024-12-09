from django.urls import path
from .views import *
from .api import PostSerializer, PostList, PostCreate
urlpatterns = [
    path('list', PostList.as_view()),
    path('detail/<str:pk>', PostDetail),
    path('create', PostCreate.as_view()),
    path('update/<str:pk>', PostUpdateView, name='post-update'),
    path('delete/<str:pk>', PostDeleteView, name='post-delete'),

]