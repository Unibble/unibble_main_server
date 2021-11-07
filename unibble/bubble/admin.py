from django.contrib import admin
from .models import Bubble,Comment
# Register your models here.
@admin.register(Bubble)
class BubbleAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass