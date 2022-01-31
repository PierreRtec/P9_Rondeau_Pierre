from django.urls import path
from . import views
from awebapp import views

app_name = "awebapp"
urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("signup/", views.signup, name="signup"),
    path("base/", views.base, name="base"),
    path("login/", views.auth_login, name="login"),
    path("logout/", views.auth_logout, name="logout"),
    path("flux/", views.flux, name="flux"),
    path("posts/", views.posts, name="posts"),
    path("abos/", views.abos, name="abos"),
    path("create-ticket/", views.create_ticket, name="create-ticket"),
    path("update-ticket/<int:review_id>", views.update_ticket, name="update-ticket"),
    path("update-review/<int:review_id>", views.update_review, name="update-review"),
    path("create-review/", views.create_review, name="create-review"),
    path("create-review-ticket/", views.create_review_ticket, name="create-review-ticket"),
    # path('view_posts/', views.view_posts, name='view_posts'),
    # path('create_review_ticket/', views.create_review_ticket, name='create_review_ticket'),
    # path('create_review/', views.create_review, name='create_review'),
    # path('create-ticket/', views.create-ticket, name='create-ticket'),
    # path('remove_user_follow/', views.remove_user_follow, name='remove_user_follow'),
    # path('add_user_follow/', views.add_user_follow, name='add_user_follow'),
    # path('update-ticketket/', views.update-ticketket, name='update-ticketket'),
    # path('update_review/', views.update_review, name='update_review'),
]