from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    re_path(r"videos/watch/(?P<video_id>\b\w{8}\b)", Video.as_view(), name="watch_video"),
    path("videos/upload", UploadVideo.as_view(), name="upload_video"),
]