from django.shortcuts import render
from .models import Book

# Create your views here.
def library(request):
    books=Book.objects.all()
    return render(request,
                  template_name='library/library.html',
                  context={'books':books}
                  )
def detail(request, pk):
    book=Book.objects.get(pk=pk)
    return render(request,
                  'library/detail.html',
                  context={'book2':book})

