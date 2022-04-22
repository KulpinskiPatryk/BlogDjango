from django.contrib import admin
from .models import *

admin.site.register(contactForm)
admin.site.register(beforeUser)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'dateOfPublish')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', "post", 'body')
# Register your models here.
