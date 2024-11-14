from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .serializers import *
from .models import *


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostSerializer



class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer


class PostRetriveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Post.objects.all()
