from django.urls import path

from posts.views import PostListView, PostDetailView, TagListView, TagDetailView, TagCreate, PostCreate, TagUpdate, \
    TagDelete, post_delete, PostUpdate, search

urlpatterns = [
    path('tags/', TagListView.as_view(), name='tags_list'),
    path('tags/create/',TagCreate.as_view(), name='tag_create'),
    path('tags/<slug:url>/', TagDetailView.as_view(), name='tag_detail'),
    path('tags/<slug:url>/update/', TagUpdate.as_view(), name='tag_update'),
    path('tags/<slug:url>/delete/', TagDelete.as_view(), name='tag_delete'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/',PostCreate.as_view(), name='post_create'),

    path('posts/<slug:url>/delete/', post_delete, name='post_delete'),
    path('posts/<slug:url>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug:url>/update/', PostUpdate.as_view(), name='post_update'),
    path('search/', search, name='search'),


]
