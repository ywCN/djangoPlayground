from django.conf.urls import url, include
from . import views  # import from local packages

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact/', views.contact, name = 'contact'),  # ^contact/$ works too, and use $ is better because only correct typed url will go to /contact page
    
    ]