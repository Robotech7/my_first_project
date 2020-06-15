from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'image')
    ordering = ('date',)
    list_filter = ('date',)
    list_editable = ('image',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text')
    ordering = ('created', )
    list_filter = ('created', 'post')
