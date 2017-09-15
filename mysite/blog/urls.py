from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [ url(r'^blog/', ListView.as_view(queryset=Post.object.all().order_by("-date")[:25],
template_name="blog/blog.html"))]