from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'single_pages/landing.html',
                  context=
                  {'title':'landing',
                    'name':'김은총'}
                  )
def aboutme(request):
    return render(request, 'single_pages/aboutme.html',
                  context=
                  {'title':'aboutme',
                    'name':'김은총'}
                  )