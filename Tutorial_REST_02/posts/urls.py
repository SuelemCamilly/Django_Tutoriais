# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),  # Rota para listar e criar posts
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Rota para detalhes de um post
]
