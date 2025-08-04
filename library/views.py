from django.shortcuts import render,redirect
from .models import Book
from .forms import Bookform

# Create your views here.
def library(request):
    books=Book.objects.all().order_by('-pk')
    return render(request,
                  template_name='library/library.html',
                  context={'books':books}
                  )
def detail(request, pk):
    book=Book.objects.get(pk=pk)
    return render(request,
                  'library/detail.html',
                  context={'book2':book})

def create(request):
    if request.method =="POST":
        bookform=Bookform(request.POST,request.FILES)
        if bookform.is_valid():
            book1=bookform.save(commit=False)
            book1.author+=' 作'
            book1.save()
            return redirect('/library/')
    else:
        bookform=Bookform()
    return render(request,
                  'library/bookform.html',
                  context={'bookform':bookform})


