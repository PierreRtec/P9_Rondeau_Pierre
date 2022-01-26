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
    path("subscrip/", views.subscrip, name="subscrip"),
    path('flux/', views.flux, name='flux'),
    path('posts/', views.posts, name='posts'),
    # path('page5/', views.p5, name='p5'),
    # path('page6/', views.p6, name='p6'),
    # path('page7/', views.p7, name='p7'),
    # path('page8/', views.p8, name='p8'),
    # path('page9/', views.p9, name='p9'),
    # path('page10/', views.p10, name='p10'),
]