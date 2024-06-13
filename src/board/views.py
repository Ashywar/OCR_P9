from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from board.forms import UserSearchForm
from reviews.models import Ticket, Review
from django.db.models import CharField, Value
from itertools import chain
from board.models import FollowersCount
from account.models import User


@login_required
def main_board(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()

    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    follows = FollowersCount.objects.filter(user=request.user)

    return render(request, "flux.html", context={"posts": posts, "follows": follows})


@login_required
def posts_page(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()

    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    return render(request, "posts.html", context={"posts": posts})


@login_required
def subscription_page(request):
    followform = UserSearchForm()
    users = User.objects.all()

    if request.method == "POST":
        form = UserSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data.get("search_query")
            followed_user = User.objects.get(username=search_query)
            if followed_user != request.user:
                try:
                    FollowersCount.objects.create(
                        user=request.user, followed_user=followed_user
                    )
                except Exception:
                    pass

    follows = FollowersCount.objects.filter(user=request.user)
    followers = FollowersCount.objects.filter(followed_user=request.user)

    return render(
        request,
        "subscription.html",
        context={
            "followform": followform,
            "follows": follows,
            "followers": followers,
            "users": users,
        },
    )


def unfollow(request, id):
    follow = FollowersCount.objects.get(pk=id)
    actual_follow = FollowersCount.objects.filter(
        user=follow.user, followed_user=follow.followed_user
    )
    actual_follow.delete()

    return redirect("/board/subscription")
