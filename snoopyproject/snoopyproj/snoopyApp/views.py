from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse
from django.template import loader
from .models import Post,Comment, Character
from .forms import CommentForm, PostForm

from django.shortcuts import render
from .models import Post, Character


def index(request):
    characters = Character.objects.all()
    selected_characters = request.GET.getlist('characters')

    if selected_characters and '' not in selected_characters:
        posts = Post.objects.filter(characters__in=selected_characters)
    else:
        # Si aucune option n'est sélectionnée ou si une option vide est présente,
        # affichez tous les postes
        posts = Post.objects.all()

    context = {
        'posts': posts,
        'characters': characters,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('index')


def post(request,id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form["body"].value()

            comment = Comment(content=content, post=post)
            comment.save()

    form = CommentForm()

    comments = Comment.objects.filter(post=post.id)
    template = loader.get_template('post.html')
    context = {
        'post': post,
        'comments':comments,
        'form':form
    }
    return HttpResponse(template.render(context, request))

def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = PostForm()
    return render(request, 'addPost.html', {'form': form})



def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    post_id = comment.post.id

    comment.delete()
    return redirect('post', id=post_id)


def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST,
                           instance=comment)
        if form.is_valid():
            content = form["body"].value()
            comment.content = content
            comment.save()

            return redirect('post', id=comment.post.id)
    else:
            form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})