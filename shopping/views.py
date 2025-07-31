from django.shortcuts import render
from .models import Shop
# Create your views here.
def shopping(request):
    shops=Shop.objects.all()
    return render(request,
                  template_name='shopping/shopping.html',
                  context={'shops':shops}
                  )