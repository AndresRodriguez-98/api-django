from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from api.users.models import SocialUser, Publication, Follow


@admin.register(User)
class UserAdmin(UserAdmin):
    pass

@admin.register(SocialUser)
class SocialUserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "nick_name",
        "role",
        "created_at",
        "email",
        "user"
    ]
    list_select_related = [
        "user"
    ]

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "follower",
        "followed",
        "created_at",
    ]
    list_select_related = [
        "follower",
        "followed"
    ]

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "text",
        "created_at",
        "user"
    ]
    list_select_related = [
        "user"
    ]
