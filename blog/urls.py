from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post-detial/<str:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path('post_detail', pk=post.pk, views.PostDetail.as_view(), name='post_detail'),
    # typo "detial --> detail", but DN work if fixed (NoReverseMatch Error)
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
