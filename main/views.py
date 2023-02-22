from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(View):
    def get(self, request):
        return render(request, "home.html")
    
class UploadVideo(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "video/upload.html")
    
    def post(self, request):
        return redirect("upload_video")

class Video(View):
    def get(self, request, video_id):
        return render(request, "video/view.html", {
            "video_id": video_id,
        })
    
    def post(self, request):
        return redirect("watch_video")