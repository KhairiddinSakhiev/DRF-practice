from django.urls import path
from .views import *


urlpatterns = [
    path("posts", PostListAPIView.as_view(), name="Post"),
    path("posts/create", PostCreateAPIView.as_view(), name="Post"),
    path("posts/detail/<int:pk>", PostRetriveAPIView.as_view(), name="Post"),
    path("posts/update/<int:pk>", PostRetriveUpdateAPIView.as_view(), name="Post"),
    path("posts/delete/<int:pk>", PostDestroyAPIView.as_view(), name="Post"),
]
