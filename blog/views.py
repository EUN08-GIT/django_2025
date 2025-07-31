from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here


def index(request):
    posts=Post.objects.all().order_by('-pk')
    return render(request,
                  'blog/index.html',
                  context={'posts':posts}
                  )
def detail(request, pk):
    post=Post.objects.get(pk=pk)
    return render(request,
                  'blog/detail.html',
                  context={'post2':post})
def create(request):
    if request.method =="POST":
        postform=PostForm(request.POST,request.FILES)
        if postform.is_valid():
            post1=postform.save(commit=False)
            post1.title+='!!'
            post1.save()
            return redirect('/blog/')
    else:
        postform=PostForm()
    return render(request,
                  template_name='blog/postform.html',
                  context={'postform':postform})


def createfake(request):
    post=Post()
    post.title='새싹 용산구'
    post.content='나진상가'
    post.save()
    return redirect('/blog/')