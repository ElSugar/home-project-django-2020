from django.urls import path
from .views import UserRegisterView, UserEditView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView, PostView
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('register', UserRegisterView.as_view(), name='register'),
  path('edit-profile', UserEditView.as_view(), name='edit-profile'),
  path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show-profile-page'),
  path('<int:pk>/profile/edit', EditProfilePageView.as_view(), name='edit-profile-page'),
  path('create-profile-page', CreateProfilePageView.as_view(), name='create-profile-page'),

  path('<int:pk>/posts', PostView, name='show-posts'),
]