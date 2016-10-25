from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/index.html', {'posts': posts})


def artigo_detalhe(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/artigo_detalhe.html', {'post':post})

def artigo_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('onetechblog.views.artigo_detalhe', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/artigo_edit.html', {'form': form})


def artigo_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('blog.views.artigo_detalhe', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/artigo_edit.html', {'form': form})

def artigo_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/artigo_draft_list.html', {'posts': posts})

def artigo_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('artigo_detalhe', pk=pk)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def artigo_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')