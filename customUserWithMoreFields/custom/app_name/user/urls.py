from django.conf.urls import url
from app_name.user.views import UserRegistrationView, UserLoginView
from app_name.profile.views import UserProfileView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    url(r'^profile', UserProfileView.as_view()),
    ]