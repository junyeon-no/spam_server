from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    print('-----------------------------')
    print(queryset)
    print('-----------------------------')
    serializer_class = PostSerializer
    print('-----------------------------')
    print(serializer_class)
    print('-----------------------------')


