from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import LogoutView

app_name = 'social'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='social/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='social/logout.html'), name='logout'),
     path('logout/', LogoutView.as_view(), name='logout'),

    # Posts
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),

    # Profiles
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
