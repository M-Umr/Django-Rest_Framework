from django.urls import include, re_path
from app_name.user.views import UserRegistrationView, UserLoginView
from app_name.profile.views import UserProfileView

urlpatterns = [
    re_path(r'^signup', UserRegistrationView.as_view()),
    re_path(r'^signin', UserLoginView.as_view()),
    re_path(r'^profile', UserProfileView.as_view()),
]