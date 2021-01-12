from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('create-post', AddPostView.as_view(), name='create-post'),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),

    path('category/<str:cats>', CategoryView, name='category'),
    path('category-list', CategoryListView, name='category-list'),
    path('add-category', AddCategoryView.as_view(), name='add-category'),

    path('like/<int:pk>', LikeView, name='like-post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),
]