from django.urls import path
from .views import *
urlpatterns = [
    path('list', PostListView),
    path('detail/<int:pk>', PostDetail),
    path('create', PostCreateView),
    path('update/<int:pk>', PostUpdateView),
    path('delete/<int:pk>', PostDeleteView),
]
