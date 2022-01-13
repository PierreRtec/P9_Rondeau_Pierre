from django.urls import path
from . import views
from awebapp import views

app_name = "awebapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("homepage/", views.homepage, name="homepage"),
    path("signup/", views.signup, name="signup"),
<<<<<<< HEAD
    path("base/", views.base, name="base"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("subscrip/", views.subscrip, name="subscrip"),

=======
    path("navbase/", views.navbase, name="navbase"),
>>>>>>> e803522f7a10a37cdec6ad57e2b5db85a90e40a4
    # path('page3/', views.p3, name='p3'),
    # path('page4/', views.p4, name='p4'),
    # path('page5/', views.p5, name='p5'),
    # path('page6/', views.p6, name='p6'),
    # path('page7/', views.p7, name='p7'),
    # path('page8/', views.p8, name='p8'),
    # path('page9/', views.p9, name='p9'),
    # path('page10/', views.p10, name='p10'),
]