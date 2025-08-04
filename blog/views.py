from django.shortcuts import render, redirect
from .models import Post, Category,Comment
from .forms import PostForm, CommentForm
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
    commentform=CommentForm()
    comment=Comment.objects.filter(post=post)

    return render(request,
                  'blog/detail.html',
                  context={'post2':post,
                           'categories':categories,
                           'comment':comment,
                          'commentform':commentform},
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

def delete(request, pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

def update(request, pk):
    post=Post.objects.get(pk=pk)
    if request.method =="POST":
        postfrom=PostForm(request.POST,request.FILES,instance=post)
        if postfrom.is_valid():
            postfrom.save()
            return redirect('/blog/')
    else:
        postform=PostForm(instance=post)

    return render(request,
                  template_name='blog/postupdate.form.html',
                  context={'postform':postform,})


def createComment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        commentform = CommentForm(request.POST, request.FILES)
        if commentform.is_valid():
            comment1 = commentform.save(commit=False)
            comment1.post = post
            comment1.save()
            return redirect(f'/blog/{post.pk}/')
    else:
        commentform = CommentForm()

    return render(request, template_name='blog/commentform.html', context={'commentform': commentform})

def updateComment(request, pk):
    comment=Comment.objects.get(pk=pk)
    post = comment.post
    if request.method =="POST":
        commentform=CommentForm(request.POST,instance=comment)
        if commentform.is_valid():
            commentform.save()
            return redirect(f'/blog/{post.pk}/')
    else:
        commentform=CommentForm(instance=comment)

    return render(request,
                  template_name='blog/updatecomment.html',
                  context={'commentform':commentform}
                  )

def deleteComment(request, pk):
    comment=Comment.objects.get(pk=pk)
    #post=comment.post
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')


