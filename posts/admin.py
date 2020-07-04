from django.contrib import admin

# Register your models here.
# from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.post)
class PhotoAdmin(admin.ModelAdmin):
    """Admin for photos."""


# @admin.register(models.User)
# class CustomUserAdmin(UserAdmin):
#     """Custom user admin."""

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    """Admin for Likes."""


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin for Comments."""
