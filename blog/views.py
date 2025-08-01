from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm
# Create your views here


def index(request):
    posts=Post.objects.all().order_by('-pk')
    categories=Category.objects.all().order_by('-pk')
    return render(request,
                  'blog/index.html',
                  context={'posts':posts,
                           'categories':categories}
                  )
def category(request, slug):
    categories = Category.objects.all()
    if slug == 'no_category':
        posts=Post.objects.filter(category=None)
    else:
        category=Category.objects.get(slug=slug)
        posts=Post.objects.filter(category=category)
    return render(request,
                  template_name='blog/index.html',
                  context={'posts':posts,
                  'categories':categories})


def detail(request, pk):
    post=Post.objects.get(pk=pk)
    categories=Category.objects.all()
    return render(request,
                  'blog/detail.html',
                  context={'post2':post,
                           'categories':categories},
                  )
def create(request):
    categories=Category.objects.all()
    if request.method =="POST":
        postform=PostForm(request.POST,request.FILES)
        if postform.is_valid():
            post1=postform.save(commit=False)
            post1.save()
            return redirect('/blog/')
    else:
        postform=PostForm()
    return render(request,
                  template_name='blog/postform.html',
                  context={'postform':postform,
                           'categories':categories})


def createfake(request):
    post=Post()
    post.title='새싹 용산구'
    post.content='나진상가'
    post.save()
    return redirect('/blog/')