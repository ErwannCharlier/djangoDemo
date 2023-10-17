from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post,Comment
#from .forms import CommentForm

def index(request):
    posts = Post.objects.all().values()

    template = loader.get_template('index.html')
    context = {
        'posts': posts ,
    }
    return HttpResponse(template.render(context, request))

def post(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post.id)
    template = loader.get_template('post.html')
    context = {
        'post': post,
        'comments':comments
    }
    return HttpResponse(template.render(context, request))

def createComment(request):
    x = request.POST['comment']
    y = request.POST['postid']
    print(x)
