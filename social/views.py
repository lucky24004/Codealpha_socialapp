from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, PostForm, CommentForm
from .models import Post, Comment, Like, Follow
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import PostForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('social:home')
#     else:
#         form = SignUpForm()
#     return render(request, 'social/signup.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile.objects.create(user=user)  # ❌ remove this
            login(request, user)
            return redirect('social:home')
    else:
        form = UserCreationForm()
    return render(request, 'social/signup.html', {'form': form})


@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('social:home')
    else:
        form = PostForm()
    return render(request, 'social/home.html', {'posts': posts, 'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('social:home')

@login_required
def follow_user(request, user_id):
    target = get_object_or_404(User, id=user_id)
    follow, created = Follow.objects.get_or_create(follower=request.user, following=target)
    if not created:
        follow.delete()
    return redirect('social:home')
# social/views.py (example)
def user_login(request):
    next_url = request.GET.get('next') or request.POST.get('next') or reverse('social:home')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.POST.get('next') or 'social:home')
        else:
            error = "Invalid credentials"
    return render(request, 'social/login.html', {'error': error, 'next': next_url})

@login_required
def user_logout(request):
   # if request.method == 'POST':
    logout(request)
    return redirect('social:home')   # change to your desired page
    # if you want to support GET (not recommended), uncomment:
    # logout(request)
    # return redirect('social:home')
   # return redirect('social:home')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Profile
from .forms import PostForm, SignUpForm
from django.contrib.auth import login, logout

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('social:home')
    else:
        form = PostForm()
    return render(request, 'social/home.html', {'posts': posts, 'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        post.delete()
    return redirect('social:home')

@login_required
def profile(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    posts = Post.objects.filter(user=user_profile.user).order_by('-created_at')
    return render(request, 'social/profile.html', {'profile': user_profile, 'posts': posts})

def user_logout(request):
    logout(request)
    return redirect('social:login')
def profile_view(request):
    return render(request, 'social/profile.html', {'user': request.user})
# def edit_profile(request):
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             request.user.email = form.cleaned_data.get('email')
#             request.user.save()
#             return redirect('social:profile')
#     else:
#         form = ProfileForm(instance=profile, initial={'email': request.user.email})
#     return render(request, 'social/edit_profile.html', {'form': form})
def edit_profile(request):
    profile = request.user.profile  # linked one-to-one profile
    if request.method == 'POST':
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        profile.bio = bio
        request.user.email = email
        request.user.save()
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('social:profile')
    return render(request, 'social/edit_profile.html', {'profile': profile})
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('social:login')
