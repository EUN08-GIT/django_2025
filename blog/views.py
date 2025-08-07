from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Category,Comment
from .forms import PostForm, CommentForm
# Create your views here

#####################################CBV#########################################
class PostListView(ListView):
    model = Post
    ordering = ['-pk']



    #template_name='/blog/post_list.html
    #context->post를->post_list
    #Comment->comment_list

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','category','uploaded_img','uploaded_file']

    def form_valid(self, form):
        current_user=self.request.user
        if current_user.is_authenticated:
            form.instance.author=current_user
            return super(PostCreateView, self).form_valid(form)
        else:
            return redirect('/blog/')

class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content','category','uploaded_img','uploaded_file']


class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'
    #template_name = 'blog/post_confirm_delete.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



#####################################FBV#########################################
def index(request):
    posts=Post.objects.all().order_by('-pk')
    categories=Category.objects.all()
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


@login_required(login_url='/accounts/google/login/')
def detail(request, pk):
    post=Post.objects.get(pk=pk)
    categories=Category.objects.all()
    comment=Comment.objects.filter(post=post)
    commentform = CommentForm()

    return render(request,
                  'blog/detail.html',
                  context={'post':post,
                           'categories':categories,
                           'comments':comment,
                          'commentform':commentform},
                  )

@login_required(login_url='/accounts/google/login/')
def create(request):
    categories=Category.objects.all()
    if request.method =="POST":
        postform=PostForm(request.POST,request.FILES)
        if postform.is_valid():
            post1=postform.save(commit=False)
            post1.author = request.user
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


@login_required(login_url='/accounts/google/login/')
def delete(request, pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

@login_required(login_url='/accounts/google/login/')
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


@login_required(login_url='/accounts/google/login/')
def createComment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        commentform = CommentForm(request.POST, request.FILES)
        if commentform.is_valid():
            comment1 = commentform.save(commit=False)
            comment1.author = request.user
            comment1.post = post
            comment1.save()
            return redirect(f'/blog/{post.pk}/')
    else:
        commentform = CommentForm()

    return render(request, template_name='blog/commentform.html', context={'commentform': commentform})

@login_required(login_url='/accounts/google/login/')
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

@login_required(login_url='/accounts/google/login/')
def deleteComment(request, pk):
    comment=Comment.objects.get(pk=pk)
    #post=comment.post
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')


