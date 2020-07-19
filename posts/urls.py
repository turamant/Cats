from django.urls import path

from posts.views import PostListView, PostDetailView, TagListView, TagDetailView, TagCreate, PostCreate, TagUpdate, \
    TagDelete, post_delete, PostUpdate, search

urlpatterns = [
    path('tags/', TagListView.as_view(), name='tags_list'),
    path('tags/create/',TagCreate.as_view(), name='tag_create'),
    path('tags/<str:url>/', TagDetailView.as_view(), name='tag_detail'),
    path('tags/<str:url>/update/', TagUpdate.as_view(), name='tag_update'),
    path('tags/<str:url>/delete/', TagDelete.as_view(), name='tag_delete'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/',PostCreate.as_view(), name='post_create'),

    path('posts/<str:url>/delete/', post_delete, name='post_delete'),
    path('posts/<str:url>/', PostDetailView.as_view(), name='post_detail'),
    #path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('posts/<slug:url>/update/', PostUpdate.as_view(), name='post_update'),
    path('search/', search, name='search'),


]
