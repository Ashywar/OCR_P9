"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account import views as account_views
from board import views as board_views
from reviews import views as reviews_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/login", account_views.login_page),
    path("account/signup", account_views.sign_up_page),
    path("account/logout", account_views.logout_user),
    path("", board_views.main_board),
    path("board/", board_views.main_board),
    path("board/subscription", board_views.subscription_page),
    path("board/posts", board_views.posts_page),
    path("reviews/create", reviews_views.create_review, name="review"),
    path("reviews/request", reviews_views.request_review, name="request"),
    path("reviews/reply/<int:id>/", reviews_views.reply_ticket, name="reply"),
    path(
        "reviews/deleteticket/<int:id>/",
        reviews_views.delete_ticket,
        name="delete-ticket",
    ),
    path(
        "reviews/deletereview/<int:id>/",
        reviews_views.delete_review,
        name="delete-review",
    ),
    path(
        "reviews/modifyticket/<int:id>/",
        reviews_views.modify_ticket,
        name="modify-ticket",
    ),
    path(
        "reviews/modifyreview/<int:id>/",
        reviews_views.modify_review,
        name="modify-review",
    ),
    path(
        "board/subscription/unfollow/<int:id>/", board_views.unfollow, name="unfollow"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
