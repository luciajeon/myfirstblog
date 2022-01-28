from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic
from .models import Post
from .forms import PostForm, CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk) # perhaps add?
            #return redirect('post-detial/<str:slug>/')
            #return path('post-detial/<str:slug>/', views.PostDetail.as_view(), name='post_detail')
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
