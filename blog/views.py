from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    #lista de entradas del blog que han sido publicadas y ordenadas por published_date
    #si el post no tiene dato en published_date no se muestra
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    #lista todos los post
    #posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posteos': posts})

def post_detail(request, id_post):
    #si no existe post nos envia a Page not found (404)
    post = get_object_or_404(Post, pk=id_post)
    return render(request, 'blog/post_detail.html', {'post': post})

#request.FILES porque recibe una imagen
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ver_post', id_post=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#request.FILES porque recibe una imagen
def post_edit(request, id_post):
    post = get_object_or_404(Post, pk=id_post)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ver_post', id_post=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})