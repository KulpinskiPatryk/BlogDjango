from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("Login/", views.Login, name="Login"),
    path("Logout/", views.Logout, name="Logout"),
    path("authorize/", views.authorize, name="authorize"),
    path("seeContact/", views.seeContactForms, name="seeContact"),
    path("register/", views.Register, name="register"),
    path("approve/<id>/", views.approve, name="approve"),
    path("addPost/", views.addPost, name="addPost"),
    path('ContactForm/', views.ContactForm, name="ContactForm"),
    path('<slug:id>/', views.showSinglePost, name="singlePost"),
    path('edit/<int:pk>/', views.updatePost.as_view(), name="updatePost"),
    path('delete/<int:pk>/', views.deletePost.as_view(), name="deletePost"),
    path('tag/<slug:tag_slug>/', views.index, name="post_tag"),


]
