from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    # PROFILE
    path("profile/", views.profile, name="profile"),
    path("profile/edit/<pk>", views.ProfileEditView.as_view(), name='profile_edit')
]
