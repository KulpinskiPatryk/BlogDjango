from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("addPost/", views.addPost, name="addPost"),
    path('<slug:id>/', views.showSinglePost, name="singlePost"),
    path('edit/<int:pk>/', views.updatePost.as_view(), name="updatePost"),
    path('delete/<int:pk>/', views.deletePost.as_view(), name="deletePost"),
    path('tag/<slug:tag_slug>/', views.index, name="post_tag"),

]
