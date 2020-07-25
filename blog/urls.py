from django.urls import path, include
from . import views

app_name = 'blog'
# maybe we have many apps in our project and all apps has a common html page called blog
# that's why we have specified our app name here so that if there is a Http request
# django can specified in which app in which html page to show
# pls check 'blog/all_blogs.html/'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

    # basically we can send int data through '<int:blog_id>/' so
    # that if some one goes mysite.com/blog/3/ he can read the
    # blog with id 3 and here instead 3 it can any number
]
