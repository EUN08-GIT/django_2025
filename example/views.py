from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from blog.views import createComment
from example.serializers import PostSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
def example(request):
    return render(request,
                  template_name='example/example.html')
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")

@api_view(['GET'])
def hiAPI(request):
    return Response("hi world")

#example/postAPI/pk
@api_view(['GET','DELETE','PUT'])
def postAPI(request,pk):
    if request.method == 'GET':
        post=Post.objects.get(pk=pk)
        postSerializer=PostSerializer(post)
        return Response(postSerializer.data)
    elif request.method == 'DELETE':
        post=Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        post=get_object_or_404(Post ,pk=pk)
        postSerializer=PostSerializer(post, data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data,
                            status=status.HTTP_200_OK)

    return Response(postSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def blogAPI(request):
    if request.method == 'GET':
        posts=Post.objects.all()
        postSerializer=PostSerializer(posts, many=True)
        return Response(postSerializer.data,
                        status=status.HTTP_200_OK)
    else:
        postserializer=PostSerializer(data=request.data)
        if postserializer.is_valid():
            postserializer.save()
            return Response(postserializer.data,
                            status=status.HTTP_201_CREATED)

    return Response(postserializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
