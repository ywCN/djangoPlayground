from django.conf.urls import url
from . import views  # import from current package

urlpatterns = [
    url(r'^$', views.index, name = 'index')]